from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment
from rest_framework import generics
from .serializers import CommentSerializer

def string_view(request):
    return HttpResponse('Hola desde Django 😄')

def html_view(request):
    return HttpResponse('<button>Click me!</button>')

def json_view(request):
    data = {
        'message': 'Petición exitosa',
        'role': 'admin',
        'status': 200
    }
    return JsonResponse(data=data)

def model_view(request):
    posts = list(Post.objects.values('id', 'title', 'content', 'published_at'))
    return JsonResponse(posts, safe=False)


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ManageCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer