# dept/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dept_page, name='dept_page'),  # Maps the root URL to the dept_page view
]