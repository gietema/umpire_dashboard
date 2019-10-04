from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


from .models import Metric
from users.models import User


class ListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'metrics'
    model = Metric
