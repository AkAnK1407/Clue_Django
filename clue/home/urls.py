from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('clubs/', views.clubs, name='clubs'),  # Clubs page
   path('dept/',  views.dept_page, name='dept_page'),  
]