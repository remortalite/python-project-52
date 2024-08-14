from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
