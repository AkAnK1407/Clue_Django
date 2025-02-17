from django.contrib import admin
from signup.models import Student # Import the Student model

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Columns to display in the admin list view
    search_fields = ('email',)  # Fields to enable search functionality
