"""Urls for metric"""
from django.urls import path

from . import views

app_name = "metrics"

urlpatterns = [path("", views.ListView.as_view(), name="list")]
