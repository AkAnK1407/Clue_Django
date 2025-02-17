from django.shortcuts import render


def home(request):
    return render(request, 'index.html')  # Render the home page

def clubs(request):
    return render(request, 'club_event.html')  # Render the clubs page

def dept_page(request):
    return render(request,"dept_page.html")