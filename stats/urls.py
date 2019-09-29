from django.urls import path

from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.store, name='store'),
    path('test', views.test, name='test'),
]