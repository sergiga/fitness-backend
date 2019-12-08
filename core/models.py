from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    device_updated = models.DateTimeField(null=True)

    class Meta:
        abstract = True
