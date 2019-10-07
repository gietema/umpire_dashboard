"""Views for user"""
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import UserCreationWithoutUsernameForm


def profile(request):
    """Profile page for user"""
    user = request.user
    return render(request, "users/profile.html", {"user": user})


def welcome(request):
    """Landing / user home page"""
    if request.user.is_authenticated:
        if request.user.stat_set.count() > 0:
            return render(
                request,
                "stats/stats_list.html",
                {
                    "user": request.user,
                    "stats": request.user.stat_set.all(),
                    "metrics": request.user.metrics.all(),
                },
            )
        return render(request, "users/home.html", {"user": request.user})
    return render(request, "users/welcome.html")


def register(request):
    """Register user"""
    if request.method == "POST":
        form = UserCreationWithoutUsernameForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)

            send_mail(
                "A new user registered",
                f"A new user with email {email} just signed up",
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMINS[0][1]],
                fail_silently=False,
            )

            return redirect("/")
    else:
        form = UserCreationWithoutUsernameForm()
    return render(request, "registration/register.html", {"form": form})
