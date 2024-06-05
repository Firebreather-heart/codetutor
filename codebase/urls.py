from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # type: ignore
    path('task/<uuid:id>/', views.taskview,
         name='task_detail'),  
    path('submit/<uuid:task_id>', views.SubmissionView.as_view(),
         name='submit'),  
    path('edit-submission/<uuid:id>/', views.SubmissionView.as_view(),
         name='edit_submission'),  # type: ignore
    path('delete-submission/<uuid:id>/',
         views.SubmissionView.as_view(), name="delete_submission"),
    path('comment/<uuid:task_id>', views.CommentView.as_view(),
         name='comment'),  # type: ignore
    path('edit-comment/<uuid:id>/', views.CommentView.as_view(),
         name='edit_comment'),  # type: ignore
    path('delete-comment/<uuid:id>/',
         views.CommentView.as_view(), name="delete_comment"),
]
