from functools import wraps

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SubmissionForm, CommentForm
from .models import Task, Submission, Comment
from accounts.models import Student, ClassRoom, School

# Create your views here.

def isStudent(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not isinstance(request.user, Student):
            return HttpResponseForbidden("You must be a student to access this view")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def isTaskAssignedToSchool(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('id'))
        if task.school != request.user.school:
            return render(request, '403.html', {'error': 'Task not assigned to your school'})
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@login_required
@isStudent
def index(request):
    if request.method == "GET":
        tasks = Task.objects.filter(school=request.user.school)
        return render(request, 'index.html', {'tasks': tasks})
    else:
        return reverse('home')


@isTaskAssignedToSchool
@isStudent
def taskview(request, id):
    task = get_object_or_404(Task, id=id)
    user_submissions = task.task_submissions.filter(student=request.user)
    comments = task.task_comments.all()
    form = SubmissionForm(initial={'student': request.user})
    return render(request, 'task.html', {'task': task, 'submissions': user_submissions, 'comments': comments, 'form':form})


class SubmissionView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        student = request.user if isinstance(request.user, Student) else None
        if student is not None:
            form = SubmissionForm(initial={'student': student})
            return render(request, 'submit.html', {'form': form})
        else:
            return render(request, '403.html', {'error': 'You are not a student!'})

    @login_required
    def post(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, id=task_id)
        if not isinstance(request.user, Student):
            return render(request, '403.html', {'error': 'You are not a student!'})
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                submission = form.save(commit=False)
                submission.student = request.user
                submission.task = task
                submission.save()
                messages.success(request, "Submitted successfully")
            except Exception as e:
                print(e)
                messages.error(request, "An error occured")
            return render(request, 'success.html', {'message': 'Submission successful!'})
        else:
            messages.error(request, "Submission failed, try again!")
            return render(request, 'error.html', {'error': 'Submission failed!'})

    @login_required
    def put(self, request, id, *args, **kwargs):
        if not isinstance(request.user, Student):
            return render(request, '403.html')
        submission = get_object_or_404(Submission, id=id, student=request.user)
        if not submission:
            return render(request, '404.html')
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.save()
            messages.success(request, 'Submission updated successfully')

        else:
            messages.error(request, 'update failed, try again')

    def delete(self, request, id, *args, **kwargs):
        if not isinstance(request.user, Student):
            return render(request, '404.html')
        submission = get_object_or_404(Submission, id=id, student=request.user)
        if not submission:
            return render(request, '404.html')
        else:
            submission.delete()
            return render(request, '')


class CommentView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        student = request.user if isinstance(request.user, Student) else None
        if student is not None:
            form = CommentForm(initial={'student': student})
            return render(request, 'submit.html', {'form': form})
        else:
            return render(request, '403.html', {'error': 'You are not a student!'})

    @login_required
    def post(self, request, *args, **kwargs):
        if not isinstance(request.user, Student):
            return render(request, '404.html', {'error': 'You are not a student!'})
        form = CommentForm(request.POST, )
        if form.is_valid():
            try:
                comment = form.save(commit=False)
                comment.student = request.user
                comment.save()
                messages.success(request, "Commented successfully")
            except Exception as e:
                print(e)
                messages.error(request, 'An error occured')
            return render(request, 'success.html', {'message': 'Submission successful!'})
        else:
            messages.error(request, "Comment failed, try again!")
            return render(request, 'error.html', {'error': 'Comment failed!'})

    @login_required
    def put(self, request, id, *args, **kwargs):
        if not isinstance(request.user, Student):
            return render(request, '404.html')
        comment = get_object_or_404(Comment, id=id, student=request.user)
        if not comment:
            return render(request, '404.html')
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.student = request.user
            comment.save()
            messages.success(request, 'Submission updated successfully')

        else:
            messages.error(request, 'update failed, try again')

    def delete(self, request, id, *args, **kwargs):
        if not isinstance(request.user, Student):
            return render(request, '404.html')
        comment = get_object_or_404(Submission, id=id, student=request.user)
        if not comment:
            return render(request, '404.html')
        else:
            comment.delete()
            return render(request, '')
