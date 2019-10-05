"""Model for Stat"""
from django.db import models

from users.models import User
from metrics.models import Metric


class Stat(models.Model):
    """Model for Stat"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    value = models.FloatField()
