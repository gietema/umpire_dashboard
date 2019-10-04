from django.test import TestCase

from .models import Metric

class MetricTestCase(TestCase):
    def setUp(self):
        self.metric = Metric.objects.create(
          name="confidence",
          description="Tracks model confidence"
        )

    def test_metric_is_created(self):
        """Metrics are created"""
        metric1 = Metric.objects.get(name="confidence")
        self.assertEqual(metric1.description, "Tracks model confidence")
