"""Seed database, create metrics"""
# Generated by Django 2.2.5 on 2019-10-07 21:20

from django.db import migrations
from metrics.models import Metric

def create_metrics(apps, schema_editor):
    """Create one metric"""
    metric = Metric()
    metric.name = 'confidence'
    metric.description = 'Tracks model confidence'
    metric.save()

    metric = Metric()
    metric.name = 'Image size'
    metric.description = 'Records input image size'
    metric.save()

    metric = Metric()
    metric.name = 'Pixel intensity'
    metric.description = 'Records pixel average intensity of your images'
    metric.save()


class Migration(migrations.Migration):
    """Seed database, create metrics"""
    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_metrics)
    ]
