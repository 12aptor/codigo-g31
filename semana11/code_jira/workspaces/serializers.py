from rest_framework import serializers
from .models import (
    Workspace,
    WorkspaceMember,
)

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'
        read_only_fields = ['deleted_at']

class WorkspaceMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceMember
        fields = '__all__'
        read_only_fields = ['workspace']