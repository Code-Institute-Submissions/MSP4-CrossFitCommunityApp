from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import UserProfile, User, HeroLevels
from workouts.models import Workout, Log, MemberComment
from allauth.account.models import EmailAddress
from .forms import UserProfileForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.contrib import messages
from django.conf import settings
from datetime import date, datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models import Avg, Max, Min, Sum
from django.template import loader
from django.http import Http404, HttpResponse, JsonResponse
import decimal
import random
import urllib.request
import stripe
import json
import statistics
from workouts.views import id_list, user_list
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .templatetags.calc_functions import calc_age

# @require_POST
# def cache_payment_create_profile(request):
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe.PaymentIntent.modify(pid, metadata={
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, 'Sorry, your payment cannot be \
#             processed right now. Please try again later.')

#         return HttpResponse(content=e, status=400)


def profile(request):
    """ a view to render the profile page """
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')
    try:
        profile = UserProfile.objects.get(user=request.user)
        template = 'profiles/profile.html'
        profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=profile)
        # cat_levels = calc_level(request.user)
        hero_levels = HeroLevels.objects.get(user=request.user)
        # print(hero_levels)
        level_data = hero_levels.level_data
        general_level = hero_levels.general_level
        # print(level_data)
        cat_levels = level_data
        categories = ["Power Lifts", "Olympic Lifts", "Body Weight", "Heavy", "Light", "Long", "Speed", "Endurance"]
        year_date = date.today() - timedelta(days=365)
        month_date = date.today() - timedelta(days=30)
        week_date = date.today() - timedelta(days=7)
        user_logs_year = Log.objects.filter(user=request.user).filter(date__gt=year_date).count()
        user_logs_month = Log.objects.filter(user=request.user).filter(date__gt=month_date).count()
        user_logs_week = Log.objects.filter(user=request.user).filter(date__gt=week_date).count()
        pry = Log.objects.filter(user=request.user).filter(date__gt=year_date).filter(personal_record=True).count()
        prm = Log.objects.filter(user=request.user).filter(date__gt=month_date).filter(personal_record=True).count()
        prw = Log.objects.filter(user=request.user).filter(date__gt=week_date).filter(personal_record=True).count()
        if (user_logs_year/12) > user_logs_month:
            perf_month = "low"
        else:
            perf_month = "high"
        if (user_logs_year/52) > user_logs_week:
            perf_week = "low"
        else:
            perf_week = "high"
        context = {
            'profile': profile,
            'form': form,
            'cat_levels': cat_levels,
            'general_level': general_level,
            'categories': categories,
            "year": user_logs_year,
            "month": user_logs_month,
            "week": user_logs_week,
            "perfm": perf_month,
            "perfw": perf_week     ,
            "pry": pry,
            "prm": prm,
            "prw": prw       
        }
        return render(request, template, context)
    except UserProfile.DoesNotExist:
        return redirect(reverse('create_profile'))


@csrf_exempt
def calc_level(request):
    if request.is_ajax():
        print("CHECK")
        if request.POST["user"] == "request":
            user = request.user
        else:
            user = User.objects.get(pk=request.POST["user"])
        users = User.objects.all()
        categories = ["Power Lifts", "Olympic Lifts", "Body Weight", "Heavy", "Light", "Long", "Speed", "Endurance"]
        cat_reverse = {"Power Lifts": "PL", "Olympic Lifts": "OL", "Body Weight": "BW", "Heavy": "HE", "Light": "LI", "Long": "LO", "Speed": "SP", "Endurance": "EN"}
        cat_levels = []
        for cat in categories:
            workouts = Workout.objects.filter(workout_category=cat_reverse[cat])
            percentiles = []
            wod_level = []
            for wod in workouts:
                # percentile = getLevels(request.user, wod)
                data = getLevels(user, wod)
                percentile = data["percentile"]
                result = data["result"]
                if percentile is not None:
                    wod_level.append({"wod": wod.workout_name, "wodperc": percentile, "wodpk": wod.pk, "result": result})
                    # wod_level.append({"wod": wod.workout_name, "wodperc": percentile, "wodpk": wod.pk})
                    percentiles.append(percentile)
            if len(percentiles) >= 3:
                accuracy = "high"
            elif len(percentiles) == 2:
                accuracy = "medium"
            elif len(percentiles) == 1:
                accuracy = "low"
            else:
                accuracy = "none"
            if accuracy != "none":
                avg_percentile = round(statistics.mean(percentiles))
            else:
                avg_percentile = "none"
            cat_levels.append({"cat": cat, "perc": avg_percentile, "acc": accuracy, "wod_level": wod_level})
        print("HALFWAY " + user.username)
        avg_list = []
        for item in cat_levels:
            if item["perc"] != "none":
                avg_list.append(item["perc"])
        if len(avg_list) != 0:
            general_level = round(statistics.mean(avg_list))
        else:
            general_level = 0
        level_data = HeroLevels.objects.filter(user=user)
        level_data.update(level_data=cat_levels)
        level_data.update(general_level=general_level)
        new_levels_html = loader.render_to_string(
        'profiles/includes/herolevel.html',
        {
            "general_level": general_level,
            "cat_levels": cat_levels
        })
        data = {
            'new_levels_html': new_levels_html
        }
        print("SUCCESS "  + user.username)
        return JsonResponse(data)
    else:
        print("FAILED HERE")
        data = {"message": "Failed update"}
        return HttpResponse(json.dumps(data), content_type='application/json')


def create_profile(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == "GET":
        if UserProfile.objects.filter(user=request.user).exists():
            messages.error(request, 'Your profile is already created.')
            return redirect(reverse('profile'))
        else:
            profile_form = UserProfileForm()
            stripe_total = 999
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            template = 'profiles/create_profile.html'
            context = {
                'form': profile_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

            return render(request, template, context)
    else:
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid() and request.POST['date'] != '':
            pid = request.POST.get('client_secret').split('_secret')[0]
            new_profile = profile_form.save(commit=False)
            new_profile.birthdate = datetime.strptime(request.POST.get('date'), "%d %b %Y")
            new_profile.stripe_pid = pid
            new_profile.email = request.user.email
            new_profile.user = request.user
            new_profile.save()
            hero_l = HeroLevels()
            hero_l.user = request.user
            hero_l.general_level = 0
            hero_l.level_data = [{"cat": "Power Lifts", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Olympic Lifts", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Body Weight", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Heavy", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Light", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Long", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Speed", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}, {"cat": "Endurance", "perc": "none", "acc": "none", "wod_level": [{"wod": "none", "wodperc": "none", "wodpk": 0}]}]
            hero_l.save()
            messages.success(request, 'Profile succesfully created and payment succesfully processed! \
            Please explore and enjoy our digital hero community!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit_profile(request):
    if request.method == "GET":

        if request.user.is_authenticated:
            if not UserProfile.objects.filter(user=request.user).exists():
                messages.error(request, 'You need to create a profile first!')
                return redirect(reverse('create_profile'))
        else:
            messages.error(request, 'You need to sign in or sign up first!')
            return redirect(reverse('account_login'))

        profile = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm(instance=profile)
        template = 'profiles/edit_profile.html'
        context = {
            'form': profile_form,
        }
        return render(request, template, context)

    else:
        instance = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=instance)

        if profile_form.is_valid():
            edited_profile = profile_form.save(commit=False)
            edited_profile.email = request.user.email
            edited_profile.user = request.user
            edited_profile.save()
            messages.success(request, 'Profile succesfully updated!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
        return redirect('edit_profile')


def getLevels(user, wod):
    # check which date is exactly a year ago
    lapse_date = date.today() - timedelta(days=365)
    if Log.objects.filter(user=user, workout=wod, rx=True, date__gt=lapse_date).count() == 0:
        percentile = None
        user_result = None
        data = {
        "percentile": percentile,
        "result": user_result
        }
        return data
    ft = False
    amrap = False
    if wod.workout_type == 'FT':
        ft = True
        rank_result = 'ft_result'
        rank_result_order = 'ft_result'
    elif wod.workout_type == 'AMRAP':
        amrap = True
        rank_result = 'amrap_result'
        rank_result_order = '-amrap_result'
    else:
        rank_result = 'mw_result'
        rank_result_order = '-mw_result'
    # sort logs by date, filter for current workout, same for logs of user only; then make list of queries
    all_logs = Log.objects.all().filter(user__userprofile__gender=user.userprofile.gender).filter(workout=wod).filter(rx=True).filter(date__gt=lapse_date).order_by(f'{rank_result_order}')
    # create list of log id's max result for this workout for every user
    user_l = user_list()
    log_id_list = id_list(user_l, all_logs, wod.workout_type)
    # filter out all none max results from query
    all_logs_rank = all_logs.filter(id__in=log_id_list)
    # if all_logs_rank.filter(user=user).count() == 0:
    #     percentile = None
    #     # user_log = None
    # else:
    total_users = all_logs_rank.all().count()
    user_log = all_logs_rank.get(user=user)
    user_result = getattr(user_log, rank_result)
    if ft:
        filter_dict = {f'{rank_result}__gte':user_result}
        greater_users = all_logs_rank.filter(**filter_dict).count()
        percentile = round(greater_users/total_users*100)
    else:
        filter_dict = {f'{rank_result}__lte':user_result}
        greater_users = all_logs_rank.filter(**filter_dict).count()
        percentile = round(greater_users/total_users*100)
    user_result = str(user_result)
    if ft:
        while user_result[0] == "0" or user_result[0] == ":":
            user_result = user_result[1:]
    else:
        while (user_result[-1] == "0" and "." in user_result) or user_result[-1] == ".":
            user_result = user_result[0:-1]
        if amrap:
            user_result = user_result + " rounds"
        else:
            user_result = user_result + "kg"
    data = {
        "percentile": percentile,
        "result": user_result
        }
    print(user)
    # return percentile
    return data
    # rank = 0
    # prevresult = [0, 0]
    # # all_gender_index = 1
    # rlistgenderall = []
    # user_rank = 0
    # for log in all_logs_rank:
    #     if getattr(log, rank_result) == prevresult[0]:
    #         prevresult[1] += 1
    #     else:
    #         rank = rank + 1 + prevresult[1]
    #         prevresult[1] = 0
    #     prevresult[0] = getattr(log, rank_result)
    #     # prevresult[0] =log.mw_result
    #     rlistgenderall.append([log.pk, rank])
    #     if log.user == user:
    #         # all_gender_index_user = all_gender_index
    #         user_rank = rank
    #     # else:
    #         # all_gender_index += 1
    # if user_rank != 0:
    #     last_rank = rlistgenderall[-1][1]
    #     percentile = round((1-(user_rank/last_rank)) * 100)
    # else:
    #     percentile = None
    # return percentile


# @csrf_exempt
# def getPersonalHistory(request):
#     page = request.POST["page"]
#     # create list of all user id's
#     member_comments = MemberComment.objects.filter(log_id__user=request.user)
#     all_logs = Log.objects.all().order_by('-date')
#     calling_group = all_logs.filter(user=request.user)
#     # user_logs[:25]
#     # check for superuser
#     no_page = False
#     superuser = False
#     if request.user.is_superuser:
#         superuser = True
#     profile = request.user
#     results_per_page = 25
#     paginator_calling_group = Paginator(calling_group, results_per_page)
#     try:
#         calling_group = paginator_calling_group.page(page)
#     except PageNotAnInteger:
#         calling_group = paginator_calling_group.page(2)
#     except EmptyPage:
#         print("ERROR LAST PAGE")
#         calling_group = paginator_calling_group.page(paginator_calling_group.num_pages)
#         no_page = True
#     calling_group_html = loader.render_to_string(
#         'profiles/includes/personal_history.html',
#         {
#         'h_group': calling_group,
#         'member_comments':member_comments,
#         'superuser': superuser,
#         "profile": profile,
#         "no_page": no_page
#         }
#     )
#     # package output data and return it as a JSON object
#     output_data = {
#         'calling_group_html': calling_group_html,
#         'has_next': calling_group.has_next()
#     }
#     return JsonResponse(output_data)