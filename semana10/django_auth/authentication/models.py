from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'roles'

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        db_column='role_id',
        related_name='users'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'users'