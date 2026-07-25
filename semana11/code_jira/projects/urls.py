from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectView.as_view()),
    path('projects/<int:pk>/', views.ManageProjectView.as_view()),
    path('projects/<int:project_id>/issues/', views.ProjectIssuesView.as_view()),
    path('issues/', views.IssueView.as_view()),
]