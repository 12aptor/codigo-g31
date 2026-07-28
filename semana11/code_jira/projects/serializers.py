from rest_framework import serializers
from .models import (
    Project,
    Issue,
    Tag,
    Attachment,
)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['deleted_at']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
        read_only_fields = ['uploaded_at', 'uploader']

class IssueSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    uploaded_files = serializers.ListField(
        child=serializers.FileField(
            max_length=100000,
            allow_empty_file=False,
            use_url=False
        ),
        write_only=True,
        required=False
    )

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['deleted_at']

    def create(self, validated_data):
        print(validated_data)
        uploaded_files = validated_data.pop('uploaded_files', [])

        request = self.context.get('request')
        uploader = request.user

        issue = Issue.objects.create(**validated_data)

        for file in uploaded_files:
            Attachment.objects.create(
                issues=issue,
                file=file,
                uploader=uploader
            )

        return issue

class IssueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['status']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
