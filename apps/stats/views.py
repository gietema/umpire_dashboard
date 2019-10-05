"""Views for stats"""
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from metrics.models import Metric
from users.models import User
from .models import Stat


@csrf_exempt
def store(request):
    """Allow users to post stats via `model.predict()`. Stores metric"""
    user = get_object_or_404(User, api_key=request.POST.get("api_key"))
    metric = get_object_or_404(Metric, name=request.POST.get("type"))

    if not user.metrics.filter(pk=metric.id).exists():
        user.metrics.add(metric.id)

    stat = Stat()
    stat.user_id = user.id
    stat.metric_id = metric.id
    stat.value = request.POST.get("stat")
    stat.save()

    return HttpResponse("")
