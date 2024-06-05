from django.contrib import admin
from .models import Task,Submission
# Register your models here.

class SubmissionInline(admin.StackedInline):
    model = Submission

class TaskAdmin(admin.ModelAdmin):
    model = Task 
    inlines = [SubmissionInline]

admin.site.register(Task, TaskAdmin)
