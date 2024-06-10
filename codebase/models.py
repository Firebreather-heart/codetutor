import uuid
from django.contrib.sessions.backends import file
from django.db import models
from accounts.models import School, Student, ClassRoom
# Create your models here.


class Task(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='school')
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name='classroom')
    date_assigned = models.DateTimeField(auto_now=True)
    date_due = models.DateTimeField(null=True, blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Task for {self.school.name} assigned on {self.date_assigned.strftime('%d-%m-%y')} due on {self.date_due.strftime('%d-%m-%y')}"

    def save(self, *args, **kwargs):
        if self.school != self.classroom.school:
            raise Exception(
                "Cannot assign task for another school to a classroom in another school")
        return super().save(*args, **kwargs)


class Submission(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_submissions')
    date_submitted = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='submission_images/', null=True, blank=True)
    file = models.FileField(
        upload_to='submission_files/', null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.task.school.name} on {self.date_submitted.strftime('%d-%m-%y')} for task {str(self.task)}"

    def save(self, *args, **kwargs):
        if self.student.school != self.task.school:
            raise Exception("Cannot submit assignment for another school")
        if self.student.classroom != self.task.classroom:
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
        if self.student.classroom != self.task.classroom:
            raise Exception(
                'cannot comment on task assigned to another classroom')
        return super().save(*args, **kwargs)
