"""Views for metrics"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Metric


class ListView(LoginRequiredMixin, generic.ListView):
    """Index view"""

    context_object_name = "metrics"
    model = Metric
