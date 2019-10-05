from django.urls import include, path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("profile/", views.profile, name="profile"),
    path("register", views.register, name="register"),
]
