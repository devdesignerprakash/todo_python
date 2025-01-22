from django.contrib import admin
from .models import*

@admin.register(TaskManager)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'deadline', 'created_at', 'updated_at']
    search_fields = ['name', 'desc']
    list_filter = ['deadline']
