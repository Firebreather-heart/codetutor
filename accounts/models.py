import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    CLASS_CHOICES = ('PR','Primary'), ('JSS', 'Junior Secondary'), ('SSS', 'Senior Secondary')
    class_name = models.CharField(max_length=100, choices=CLASS_CHOICES)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='classrooms')
    
    def __str__(self):
        return f'{self.class_name} - {self.school.name}'

class CustomClassRoom(models.Model):
    class_name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='custom_classrooms')
    
    def __str__(self):
        return f'{self.class_name} - {self.school.name}'


class Student(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    custom_classroom = models.ForeignKey(
        CustomClassRoom, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    groups = models.ManyToManyField(Group, related_name='student_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='student_user_set')

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.custom_classroom is None and self.classroom is None:
            raise ValueError('Student must belong to a classroom or custom classroom')
        super().save(*args, **kwargs)
    


class CustomUser(AbstractUser):
    email = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_user_set')

    def __str__(self):
        return self.username
