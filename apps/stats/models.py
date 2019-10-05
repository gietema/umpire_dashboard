from django.db import models

from users.models import User
from metrics.models import Metric

import numpy as np
import json


class Stat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    value = models.FloatField()

    def all_vals(self) -> np.ndarray:
        return np.array(
            list(
                Stat.objects.filter(metric=self.metric_id).values_list(
                    "value", flat=True
                )
            )
        )

    def mean(self) -> float:
        return round(self.all_vals().mean(), 4)

    def std(self) -> float:
        return round(self.all_vals().std(), 4)

    def json_vals(self):
        return json.dumps(self.all_vals())
