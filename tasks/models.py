from django.db import models
from django.contrib.auth.models import User

from statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
