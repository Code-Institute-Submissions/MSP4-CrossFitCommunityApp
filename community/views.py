from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import CustomGroup
from profiles.models import UserProfile, User, HeroLevels
from workouts.models import Workout, Log, MemberComment
from allauth.account.models import EmailAddress
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
from profiles.templatetags.calc_functions import calc_age
import math


def roundup(x):
    return int(math.ceil(x / 10)) * 10


def rounddown(x):
    return int(math.floor(x / 10)) * 10


def community(request):
    template = "community/community.html"
    groups = CustomGroup.objects.filter(group_users=request.user)
    age = calc_age(request.user.userprofile.birthdate)
    age_bottom = str(rounddown(age))
    age_top = str(roundup(age))
    age_group = age_bottom + "-" + age_top + " years"

    context = {
        'groups': groups,
        'age_group': age_group
        }
    return render(request, template, context)