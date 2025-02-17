# from django.contrib import admin
# from django.urls import path, include
# from signup.views import signupaction
# from login.views import loginaction, profileview
# from home.views import clubs
# from dept.views import dept_page
# from login.views import logout_view  # Import the logout function




# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin panel
#     path('', include('home.urls')),  # Include URLs from the home app (for index.html)
#     path('signup/', signupaction, name='signup'),  # Signup page
#     path('login/', loginaction, name='login'),  # Login page
#     path('profile/', profileview, name='profile'),  # Profile page
#     path('dept/', dept_page, name='dept'),  # Include URLs from the dept app
#     path('event/', include('event.urls')),  # Include URLs from the event app
#     path('clubs/', clubs, name='clubs'),
#     path('logout/', logout_view, name='logout'),  # Logout page

# ]

from django.contrib import admin
from django.urls import path, include
from signup.views import signupaction , logout_view ,check_email # Added logout
from login.views import loginaction,check_login, profileview  
from home.views import clubs, home
from dept.views import dept_page


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('signup/', signupaction, name='signup'),  
    path('login/', loginaction, name='login'),  
    path('logout/', logout_view, name='logout'),  # Added logout URL
    path('profile/', profileview, name='profile'),  

    # App-related URLs
    path('home/',home,name='home'),
    path('', include('home.urls')),  # Home URLs (Ensure it doesn't overlap with `clubs`)
    path('dept/', dept_page, name='dept'),
    path('clubs/', clubs, name='clubs'),
    path('event/', include('event.urls')),  # Event-related URLs
    path('check_login/', check_login, name='check_login'),
    path('check-email/', check_email, name='check_email'),  # Add endpoint
]

