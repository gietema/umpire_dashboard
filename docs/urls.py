"""Urls for docs"""
from django.urls import path

from . import views

app_name = "docs"

urlpatterns = [path("", views.ListView.as_view(), name="list")]
