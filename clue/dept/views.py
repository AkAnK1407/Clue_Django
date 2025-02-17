from django.shortcuts import render

def dept_page(request):
    return render(request, 'dept_page.html')
