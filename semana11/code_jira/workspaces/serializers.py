from rest_framework import serializers
from .models import (
    Workspace,
    WorkspaceMember,
)
from django.contrib.auth import get_user_model

class WorkspaceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

class WorkspaceSerializer(serializers.ModelSerializer):
    members = WorkspaceUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Workspace
        fields = '__all__'
        read_only_fields = ['deleted_at']

class WorkspaceMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceMember
        fields = '__all__'

    def validate_role(self, value):
        if value == WorkspaceMember.Role.OWNER:
            raise serializers.ValidationError("No está permitido asignar el rol OWNER")
        return value