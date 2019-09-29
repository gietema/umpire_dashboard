from django.urls import path

from . import views

app_name = 'metrics'

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('api/metrics/', views.MetricListCreate.as_view() ),
]