"""umpire_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^umpire_dashboard/', include('umpire-dasboard.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import PasswordResetView

from users.views import welcome

urlpatterns = [
    path("", welcome, name="welcome"),
    path("accounts/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("metrics/", include("metrics.urls")),
    path("stats/", include("stats.urls")),
    path("docs/", include("docs.urls")),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            email_template_name="registration/password_reset_email.txt",
            html_email_template_name="registration/password_reset_email.html",
        ),
        name="password_reset",
    ),
    path("", include("django.contrib.auth.urls")),
]
