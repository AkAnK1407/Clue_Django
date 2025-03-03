from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include  # ✅ Include is necessary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signup.urls')),  # ✅ Correct path
    path('home/', include('home.urls')),  # If home is also in signup
    path('',include('home.urls')),
    path('event/',include('event.urls') ),
    path('department/',include('department.urls') ),
]
