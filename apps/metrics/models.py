"""Metrics model"""
from django.db import models

import numpy as np

from stats.models import Stat

class Metric(models.Model):
    """
        Metrics model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def stats(self) -> np.array:
        """Return numpy array of stats of model"""
        return np.array(Stat.objects.filter(metric=self.id).get('value'))

    def mean(self) -> float:
        """Return mean of stats of metric"""
        return round(self.stats().mean(), 4)

    def std(self) -> float:
        """return standard deviation of stats of metric"""
        return round(self.stats().std(), 4)
