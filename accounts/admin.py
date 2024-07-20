from django.contrib import admin
from .models import School, Student, ClassRoom, CustomClassRoom, CustomUser
from codebase.models import Task,Submission
# Register your models here.


class StudentInline(admin.TabularInline):
    model = Student

class ClassRoomInline(admin.StackedInline):
    model = ClassRoom

class CustomClassRoomInline(admin.StackedInline):
    model = CustomClassRoom

class TaskInline(admin.StackedInline):
    model = Task

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [StudentInline, ClassRoomInline, CustomClassRoomInline]


class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'school']
    list_filter = ['school']

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'school']
    inlines = [StudentInline, TaskInline]

class CustomClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'school']
    inlines = [StudentInline, TaskInline]

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    

admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(CustomClassRoom, CustomClassRoomAdmin)