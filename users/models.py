import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  username = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=255)
  phone = models.CharField(max_length=20, blank=True, null=True)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  subscription_tier = models.CharField(
    max_length = 20,
    choices = [
      ('free', 'Free'),
      ('pro', 'Pro'),
      ('enterprise', 'Enterprise'),
    ],
    default = 'free'
  )
  last_active = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.email or self.username
  
  class Meta:
    indexes = [
      models.Index(fields=['email']),
      models.Index(fields=['subscription_tier']),
    ]