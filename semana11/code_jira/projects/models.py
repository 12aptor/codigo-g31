from django.db import models
from workspaces.models import Workspace

class Project(models.Model):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='workspaces'
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
        related_name='workspaces'
    )
    name = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=7, default='#808080')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['workspace', 'name'], name='unique_tab_project')
        ]

class Issue(models.Model):
    class Status(models.TextChoices):
        BACKLOG = 'BACKLOG', 'Backlog'
        TODO = 'TODO', 'Por Hacer'
        IN_PROGRESS = 'IN_PROGRESS', 'En Progreso'
        IN_REVIEW = 'IN_REVIEW', 'En Revision'
        DONE = 'DONE', 'Completado'
        CANCELED = 'CANCELED', 'Cancelado'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.BACKLOG
    )
