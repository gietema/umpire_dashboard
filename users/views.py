from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .forms import UserCreationForm

# Create your views here.
User = get_user_model()

def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html', {'user': request.user})
    return render(request, 'users/welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})