from django import forms
from .models import Task,Submission,Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['school','date_due','desc','image', 'classroom']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student','task','image','file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['task','student','comment','hidden']