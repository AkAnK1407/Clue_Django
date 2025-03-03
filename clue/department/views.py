from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from event.models import Department
from .models import Fest, dEvent
from django.http import HttpResponse

def home(request):
    departments = Department.objects.all()
    return render(request, 'page_01.html', {'departments': departments})

def department_detail(request, department_name):
    department = get_object_or_404(Department, department_name=department_name)
    fests = Fest.objects.filter(department_name=department)  # ✅ Corrected field name
    return render(request, 'department_detail.html', {'department': department, 'fests': fests})

def Fest_detail(request, department_name, fest_name):
    try:
        department = get_object_or_404(Department, department_name=department_name)
        fests = get_object_or_404(Fest, fest_name=fest_name, department_name=department)  # ✅ Corrected field name
        return render(request, 'fest_detail.html', {'fests': fests, 'department': department})
    except (Department.DoesNotExist, Fest.DoesNotExist):
        return HttpResponse("Fest not found", status=404)

def fest_list(request, department_name):
    department = get_object_or_404(Department, department_name=department_name)
    fests = Fest.objects.filter(department_name=department)  # ✅ Corrected field name
    return render(request, "fest_detail.html", {"department": department, "fests": fests})  # ✅ Fixed template name



def fest_events(request, department_name, fest_name):
    department = get_object_or_404(Department, department_name=department_name)
    fest = get_object_or_404(Fest, fest_name=fest_name, department_name=department)
    events = dEvent.objects.filter(fest=fest)
    return render(request, 'fest_detail.html', {'department': department, 'fest': fest, 'events': events})




def event_detail(request, department_name, fest_name, event_name):
    department = get_object_or_404(Department, department_name=department_name)
    fests = get_object_or_404(Fest, fest_name=fest_name, department_name=department)
    event = get_object_or_404(dEvent, event_name=event_name, fest_name=fest_name)
    return render(request, 'eventd.html', {'department': department, 'fests': fests, 'event': event})

# Create your views here.
