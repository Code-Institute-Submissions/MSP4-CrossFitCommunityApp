from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.workouts, {'wod_id': '0'}, name='workouts'),
    path('<wod_id>/', views.workouts, name='workouts'),
    path('0/commentMember/', views.commentMember, name='commentMember'),
    path('0/deleteCommentMember/', views.deleteCommentMember, name='deleteCommentMember'),
    path('0/deleteLog/', views.deleteLog, name='deleteLog'),
    path('0/dateInput/', views.dateInput, name='dateInput'),
    path('0/editLog/', views.editLog, name='editLog'),
    path('0/loopList/', views.loopList, name='loopList'),
    path('0/loopListRank/', views.loopListRank, name='loopListRank'),
    path('0/editWorkout/', views.editWorkout, name='editWorkout'),
    path('0/createWorkout/<wod_id>/', views.createWorkout, name='createWorkout'),
    path('0/deleteWorkout/', views.deleteWorkout, name='deleteWorkout'),
    path('0/setWod/', views.setWod, name='setWod'),
    path('0/getSliderLevel/', views.getSliderLevel, name='getSliderLevel'),
]
