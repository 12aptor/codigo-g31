from rest_framework import serializers
from .models import (
    Project,
    Issue,
    Tag,
    Attachment,
)
from drf_spectacular.utils import extend_schema_field

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['deleted_at']

class AttachmentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Attachment
        fields = '__all__'
        read_only_fields = ['uploaded_at', 'uploader']

@extend_schema_field({
    "type": "array",
    "items": {
        "type": "string",
        "format": "binary"
    }
})
class MultipleImageField(serializers.ListField):
    child = serializers.FileField(allow_empty_file=False, use_url=False)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class FlexibleTagField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()

    def to_internal_value(self, data):
        if isinstance(data, int) or (isinstance(data, str) and data.isdigit()):
            try:
                return Tag.objects.get(pk=int(data))
            except Tag.DoesNotExist:
                raise serializers.ValidationError(f"Tag con ID '{data}' no existe.")
        raise serializers.ValidationError("Tipo de dato inválido para Tag.")

    def to_representation(self, value):
        return TagSerializer(value).data

class IssueSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    uploaded_files = MultipleImageField(write_only=True, required=False)
    tags = FlexibleTagField(many=True, required=False)

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'deleted_at', 'reporter']

    def to_internal_value(self, data):
        if hasattr(data, 'getlist'):
            data = data.copy()
            if 'tags' in data:
                raw_tags = data.getlist('tags')
                cleaned = []
                for item in raw_tags:
                    if isinstance(item, str):
                        if ',' in item:
                            cleaned.extend([x.strip() for x in item.split(',') if x.strip()])
                            continue
                    cleaned.append(item)
                data.setlist('tags', cleaned)
        return super().to_internal_value(data)

    def create(self, validated_data):
        uploaded_files = validated_data.pop('uploaded_files', [])
        request = self.context.get('request')
        uploader = request.user

        issue = super().create({**validated_data, 'reporter': uploader})

        for file in uploaded_files:
            Attachment.objects.create(
                issue=issue,
                file=file,
                uploader=uploader
            )

        return issue

class IssueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['status']
