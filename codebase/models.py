import uuid
from django.contrib.sessions.backends import file
from django.db import models
from accounts.models import School, Student, ClassRoom, CustomClassRoom
from cloudinary.models import CloudinaryField
# Create your models here.


class Task(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='school')
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name='classroom', null=True, blank=True)
    custom_classroom = models.ForeignKey(
        CustomClassRoom, on_delete=models.CASCADE, related_name='custom_classroom', null=True, blank=True)
    date_assigned = models.DateTimeField(auto_now=True)
    date_due = models.DateTimeField(null=True, blank=True)
    desc = models.TextField()
    image = CloudinaryField('image', blank=True,
                            null=True, folder='task_images/')
    file = CloudinaryField('file', blank=True, null=True,
                           folder='task_files/')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Task for {self.school.name} assigned on {self.date_assigned.strftime('%d-%m-%y')} due on {self.date_due.strftime('%d-%m-%y')}" 

    def save(self, *args, **kwargs):
        if self.classroom is None and self.custom_classroom is None:
            raise Exception(
                'Task must be assigned to a classroom or custom classroom')
        if self.classroom:
            if self.school != self.classroom.school:
                raise Exception(
                    "Cannot assign task for another school to a classroom in another school")
        if self.custom_classroom:
            if self.school != self.custom_classroom.school:
                raise Exception(
                    "Cannot assign task for another school to a classroom in another school")
        
        return super().save(*args, **kwargs)


class Submission(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_submissions')
    date_submitted = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True,
                            null=True, folder='submission_images/')
    file = CloudinaryField('file', blank=True, null=True,
                           folder='submission_files/')
    score = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.task.school.name} on {self.date_submitted.strftime('%d-%m-%y')} for task {str(self.task)}"

    def save(self, *args, **kwargs):
        if self.student.school != self.task.school:
            raise Exception("Cannot submit assignment for another school")
        
        if self.student.classroom:
            if self.student.classroom != self.task.classroom:
                raise Exception(
                    'cannot submit for task assigned to another classroom')
        if self.student.custom_classroom:
            if self.student.custom_classroom != self.task.custom_classroom:
                raise Exception(
                    'cannot submit for task assigned to another classroom')
        return super().save(*args, **kwargs)


class Comment(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_comments')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student_comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        if self.student.school != self.task.school:
            raise Exception(
                "Cannot comment on task assigned to another school")
        if self.student.custom_classroom:
            if self.student.classroom != self.task.classroom:
                raise Exception(
                    'cannot comment on task assigned to another classroom')
        if self.student.custom_classroom:
            if self.student.custom_classroom != self.task.custom_classroom:
                raise Exception(
                    'cannot comment on task assigned to another classroom')
        return super().save(*args, **kwargs)
