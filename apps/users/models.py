"""Model file for user"""
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model"""
    username = None
    email = models.EmailField(
        ("email"), unique=True
    )  # changes email to unique and blank to false
    api_key = models.CharField(max_length=500)
    metrics = models.ManyToManyField("metrics.Metric")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
