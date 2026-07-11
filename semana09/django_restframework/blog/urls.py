from django.urls import path
from . import views

urlpatterns = [
    path('string/', views.string_view),
    path('html/', views.html_view),
    path('json/', views.json_view),
    path('posts/', views.model_view),
    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.ManageCommentView.as_view()),
]