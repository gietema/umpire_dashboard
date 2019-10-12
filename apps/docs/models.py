"""Doc model"""
from django.db import models


class Doc(models.Model):
    """Docs model"""

    title = models.CharField(max_length=100)
    body = models.TextField()
