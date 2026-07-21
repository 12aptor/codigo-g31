from django.db import models
from django.contrib.auth import get_user_model # Primera forma
from users.models import User # Segunda forma
from django.conf import settings # Tercera forma
from projects.models import SoftDeleteModel

class Workspace(SoftDeleteModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(
        get_user_model(),
        through='WorkspaceMember',
        related_name='workspaces'
    )

    def __str__(self):
        return self.name

class WorkspaceMember(models.Model):
    class Role(models.TextChoices):
        OWNER = 'OWNER', 'Propietario'
        ADMIN = 'ADMIN', 'Administrador'
        MEMBER = 'MEMBER', 'Miembro'
        GUEST = 'GUEST', 'Invitado'

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.MEMBER
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.workspace.name} ({self.role})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'workspace'], name='unique_workspace_member')
        ]