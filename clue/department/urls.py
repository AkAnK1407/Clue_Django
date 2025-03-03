from django.urls import path
from .views import home, department_detail, Fest_detail, fest_events, event_detail

urlpatterns = [
    path('department/', home, name='department'),
    
    path('department/<str:department_name>/', department_detail, name='department_detail'),
    # path('department/<str:department_name>/fests/', department_fests, name='department_fests'),
    path('department/<str:department_name>/<str:fest_name>/', Fest_detail, name='fest_detail'),
    path('department/<str:department_name>/fests/<str:fest_name>/events/', fest_events, name='fest_events'),
    path('department/<str:department_name>/fests/<str:fest_name>/events/<str:event_name>/', event_detail, name='event_detail'),
    path('department/<str:department_name>/<str:fest_name>/<str:event_name>/', event_detail, name='event_detail'),


]