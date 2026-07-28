from rest_framework import serializers
from .models import (
    Project,
    Issue,
    Tag,
)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['deleted_at']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['deleted_at']

class IssueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['status']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'