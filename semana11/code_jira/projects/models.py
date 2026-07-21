from django.db import models
from workspaces.models import Workspace
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

class Project(SoftDeleteModel):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.workspace.name}] {self.name}"

class Tag(models.Model):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    name = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=7, default='#808080')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['workspace', 'name'], name='unique_tab_project')
        ]

class Issue(SoftDeleteModel):
    class Status(models.TextChoices):
        BACKLOG = 'BACKLOG', 'Backlog'
        TODO = 'TODO', 'Por Hacer'
        IN_PROGRESS = 'IN_PROGRESS', 'En Progreso'
        IN_REVIEW = 'IN_REVIEW', 'En Revision'
        DONE = 'DONE', 'Completado'
        CANCELED = 'CANCELED', 'Cancelado'

    class Priority(models.TextChoices):
        LOW = 'LOW', 'Baja'
        MEDIUM = 'MEDIUM', 'Media'
        HIGH = 'HIGH', 'Alta'
        URGENT = 'URGENT', 'Urgente'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='issues'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.BACKLOG
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reported_issues',
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='assigned_issues',
    )
    parent_issue = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sub_issues'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='issues'
    )
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IssueActivity(models.Model):
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    actor = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='activities'
    )
    field_changed = models.CharField(max_length=50)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        actor_name = self.actor.username if self.actor else 'Sistema'
        return f"{actor_name} cambió {self.field_changed} en {self.issue.id}"

    class Meta:
        ordering = ['-created_at']

class Attachment(models.Model):
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    uploader = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='attachments'
    )
    file = CloudinaryField('file', folder='attachments')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo para Issue #{self.issue.id}"