from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at')  # Display relevant fields in the list view
    search_fields = ('title', 'user__username')  # Allow searching by task title and associated username
    list_filter = ('completed', 'user')  # Filter tasks by completion status and user

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

