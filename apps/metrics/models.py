from django.db import models

import numpy as np


class Metric(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def stats(self) -> np.array:
        return np.array(self.stats_list())

    def mean(self) -> float:
        return round(self.stats().mean(), 4)
    
    def std(self) -> float:
        return round(self.stats().std(), 4)
    
    def stats_list(self) -> list:
        return list(self.stat_set.values_list('value', flat=True).all())