from django.shortcuts import render, redirect, reverse
from datetime import date, datetime
from .models import Workout
from .models import Log
from .forms import LogForm
from django.utils.dateparse import parse_duration
from django.db.models import Avg, Max, Min, Sum
from django.contrib import messages
# Create your views here.


def striphours(duration):
    for x in duration:
        if x == "0" or x == ':':
            no_hours = duration.split(x, 1)[1]
        else:
            break
    return no_hours


def workouts(request, wod_id):
    if wod_id == "0":
        wod = Workout.objects.get(workout_is_wod=True)
    else:
        wod = Workout.objects.get(id=wod_id)
    if request.method == "GET":
        # log = Log.objects.filter().first()
        all_logs = Log.objects.all().order_by('-date')
        all_logs_wod = all_logs.filter(wod_name=wod.workout_name)
        user_logs = all_logs.filter(user=request.user)
        user_logs_wod = user_logs.filter(wod_name=wod.workout_name)
        log_groups = [all_logs, all_logs_wod, user_logs, user_logs_wod]

        if wod.workout_type == 'FT':
            print("TEST1")
            all_logs_rank = Log.objects.filter(wod_name=wod.workout_name).order_by('ft_result')
            rank_result = 'ft_result'
        elif wod.workout_type == 'AMRAP':
            print("TEST2")
            all_logs_rank = Log.objects.filter(wod_name=wod.workout_name).order_by('-amrap_result')
            rank_result = 'amrap_result'
        else:
            print("TEST3")
            all_logs_rank = Log.objects.filter(wod_name=wod.workout_name).order_by('-mw_result')
            rank_result = 'mw_result'
        filter_rx = all_logs_rank.filter(rx=True)
        all_logs_rank_today = filter_rx.filter(date=date.today())
        print(all_logs_rank)
        rank_groups = [all_logs_rank, all_logs_rank_today]
        # if log is None:
        #     result = "No logs for this WOD"
        # else:
        #     duration = str(log.ft_result)
        #     result = striphours(duration)
        date_today = date.today()
        date_initial = date_today.strftime("%d %b %Y")
        form_log = LogForm()
        context = {
            'wod': wod,
            'all_logs': all_logs,
            'all_logs_wod': all_logs_wod,
            'user_logs': user_logs,
            'user_logs_wod': user_logs_wod,
            'log_groups': log_groups,
            'all_logs_rank': all_logs_rank,
            'all_logs_rank_today': all_logs_rank_today,
            'rank_groups': rank_groups,
            'rank_result': rank_result,
            'form_log': form_log,
            'date_initial': date_initial,
        }
        template = "workouts/workouts.html"
        return render(request, template, context)
    else:

        if wod.workout_type == 'FT':
            print("FT")
            result = 'ft_result'
            non_result_1 = 'amrap_result'
            non_result_2 = 'mw_result'
        elif wod.workout_type == 'AMRAP':
            print("AMRAP")
            result = 'amrap_result'
            non_result_1 = 'ft_result'
            non_result_2 = 'mw_result'
        else:
            print("MW")
            result = 'mw_result'
            non_result_1 = 'amrap_result'
            non_result_2 = 'ft_result'
            
        form_data = {
            f"{result}": request.POST[f"{result}"],
            f"{non_result_1}": 0,
            f"{non_result_2}": 0,
            'rx': request.POST['rx'],
            'date': datetime.strptime(request.POST.get('date'), "%d %b %Y"),
            'user_comment': request.POST['user_comment'],
        }
        
        log_form = LogForm(form_data)
        # fresult = request.POST[f"{result}"]
        if log_form.is_valid():  #  and fresult != '':
            new_log = log_form.save(commit=False)
            new_log.wod_name = wod.workout_name
            new_log.user = request.user
            if wod.workout_type == "FT":
                new_result = new_log.ft_result.seconds
                max_result = Log.objects.filter(user=request.user, wod_name=wod.workout_name).aggregate(Min('ft_result'))
                if max_result['ft_result__min'] == None:
                    new_log.personal_record = True
                else:
                    best_result = max_result['ft_result__min'].seconds
                    if best_result > new_result:
                        new_log.personal_record = True
                    else:
                        new_log.personal_record = False
            elif wod.workout_type == "AMRAP":
                new_result = new_log.amrap_result
                max_result = Log.objects.filter(user=request.user, wod_name=wod.workout_name).aggregate(Max('amrap_result'))
                if max_result['amrap_result__max'] == None:
                    new_log.personal_record = True
                else:
                    best_result = max_result['amrap_result__max']
                    if best_result < new_result:
                        new_log.personal_record = True
                    else:
                        new_log.personal_record = False
            else:
                new_result = new_log.mw_result
                max_result = Log.objects.filter(user=request.user, wod_name=wod.workout_name).aggregate(Max('mw_result'))
                if max_result['mw_result__max'] == None:
                    new_log.personal_record = True
                else:
                    best_result = max_result['mw_result__max']
                    if best_result < new_result:
                        new_log.personal_record = True
                    else:
                        new_log.personal_record = False
            new_log.save()
            messages.success(request, 'Workout logged: Great work!')
            return redirect(reverse('workouts', args=(wod_id,)))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return redirect(reverse('workouts', args=wod_id))

