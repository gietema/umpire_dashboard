from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework import generics

from .models import Metric
from users.models import User
from .serializers import MetricSerializer


class ListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'metrics'
    model = Metric

class MetricListCreate(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer