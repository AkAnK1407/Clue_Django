from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Fest, dEvent
# Register your models here.
admin.site.register(Fest)
admin.site.register(dEvent)