"""Admin of user"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    UserCreationWithoutUsernameForm,
    UserWithoutPassWordConfirmationChangeForm,
)
from .models import User


class UserWithoutUsernameAdmin(UserAdmin):
    """User admin class. Uses email instead of username"""

    add_form = UserCreationWithoutUsernameForm
    form = UserWithoutPassWordConfirmationChangeForm
    model = User
    list_display = ["email"]
    ordering = ("email",)


admin.site.register(User, UserWithoutUsernameAdmin)
