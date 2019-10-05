"""Model for Stat"""
import numpy as np

from django.db import models

from users.models import User
from metrics.models import Metric


class Stat(models.Model):
    """Model for Stat"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    value = models.FloatField()

    def all_vals(self) -> np.ndarray:
        """Get all flattened stats in numpy array"""
        return np.array(
            list(
                Stat.objects.filter(metric=self.metric).values_list(
                    "value", flat=True
                )
            )
        )

    def mean(self) -> float:
        """Rounded mean of all values"""
        return round(self.all_vals().mean(), 4)

    def std(self) -> float:
        """Rounded standard deviation of all values"""
        return round(self.all_vals().std(), 4)
