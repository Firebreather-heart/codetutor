from django.contrib import admin
from .models import School, Student, ClassRoom
from codebase.models import Task,Submission
# Register your models here.


class StudentInline(admin.TabularInline):
    model = Student

class ClassRoomInline(admin.StackedInline):
    model = ClassRoom

class TaskInline(admin.StackedInline):
    model = Task

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [StudentInline, ClassRoomInline]


class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'school']
    list_filter = ['school']

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'school']
    inlines = [StudentInline, TaskInline]




admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
