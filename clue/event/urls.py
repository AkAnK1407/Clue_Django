# event/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('event/', views.event_page, name='event_page'),
    path('dept/', views.dept_page, name='dept_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('club-event/', views.club_event, name='club_event'),
]