from django.db import models

from flow_task import settings

# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      related_name='owned_workspaces',
      on_delete=models.CASCADE
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='WorkspaceMembership',
        related_name='workspaces'
    )

    def __str__(self):
        return self.name

class WorkspaceMembership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    role = models.CharField(max_length = 50)
    joined_at = models.DateTimeField(auto_now_add=True)