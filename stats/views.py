from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Stat
from users.models import User, Metric
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

@csrf_exempt
def store(request):
    # check if api key is known
    user = get_object_or_404(User, api_key=request.POST.get('api_key'))
    metric = get_object_or_404(Metric, name=request.POST.get('type'))
    
    if user.metrics.filter(pk=metric.id).exists() == False:
        user.metrics.add(metric.id)

    stat = Stat()
    stat.user_id = user.id
    stat.metric_id = metric.id
    stat.value = request.POST.get('stat')
    stat.save()

    return HttpResponse('')

def test(request):
    return HttpResponse('test')