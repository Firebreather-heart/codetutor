from django.contrib import admin
from .models import Task,Submission
# Register your models here.

class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    model = Task 
    inlines = [SubmissionInline]
    list_display = ['school','classroom','date_assigned','date_due','desc']
    list_filter = ['school','classroom']
    ordering = ['-date_assigned']

admin.site.register(Task, TaskAdmin)
