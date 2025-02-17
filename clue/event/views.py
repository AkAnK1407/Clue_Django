from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')

def event_page(request):
    return render(request, 'event_page.html')

def dept_page(request):
    return render(request, 'dept_page.html')

def profile_page(request):
    return render(request, 'profile_page.html')

def club_event(request):
    return render(request, 'club_event.html')
# def club_event(request):
#     return render(request, 'club_event.html')
