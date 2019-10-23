"""Tests for metric"""
from django.test import Client
from django.test import TestCase

from users.models import User
from stats.models import Stat
from .models import Metric


class MetricTestCase(TestCase):
    """Tests for metric"""

    def setUp(self):
        self.metric = Metric.objects.create(
            name="test", description="Tracks model test"
        )
        self.user = User.objects.create(
            email='foo@bar.com', password="foobar", api_key='123'
        )

    def test_metric_is_created(self):
        """Metrics are created"""
        metric1 = Metric.objects.get(name="test")
        self.assertEqual(metric1.description, "Tracks model test")

    def test_metric_is_saved(self):
        """Test that metric is saved when posted"""
        client = Client()
        response = client.post('/stats/', {'api_key': '123', 'type': 'confidence', 'stat': 1})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Stat.objects.all()))
