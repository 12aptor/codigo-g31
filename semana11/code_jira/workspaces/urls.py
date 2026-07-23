from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.WorkspaceView.as_view()),
    path('workspaces/<int:pk>/', views.ManageWorkspaceView.as_view()),
    path('workspaces/members/', views.WorkspaceMemberView.as_view())
]