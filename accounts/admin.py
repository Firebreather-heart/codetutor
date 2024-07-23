from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Student, ClassRoom, CustomClassRoom, CustomUser
from codebase.models import Task, Submission
# Register your models here.


class StudentInline(admin.TabularInline):
    model = Student

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class ClassRoomInline(admin.StackedInline):
    model = ClassRoom


class CustomClassRoomInline(admin.StackedInline):
    model = CustomClassRoom


class TaskInline(admin.StackedInline):
    model = Task


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [StudentInline, ClassRoomInline, CustomClassRoomInline]


class StudentAdmin(UserAdmin):
    list_display = ['username',  'school']
    list_filter = ['school']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'school']
    inlines = [StudentInline, TaskInline]


class CustomClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'school']
    inlines = [StudentInline, TaskInline]


class CustomUserAdmin(UserAdmin):
    list_display = ['username', ]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )
    


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(CustomClassRoom, CustomClassRoomAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
