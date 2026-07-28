from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectView.as_view()),
    path('projects/<int:pk>/', views.ManageProjectView.as_view()),
    path('projects/<int:project_id>/issues/', views.ProjectIssuesView.as_view()),
    path('issues/', views.IssueView.as_view()),
    path('issues/<int:pk>/status/', views.IssueStatusView.as_view()),
    path('tags/', views.TagView.as_view())
]