# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.crypto import get_random_string
from .models import User


class UserCreationForm(UserCreationForm):
    username = None
    password2 = None

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields["password1"].help_text = "Min. 8 characters"

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save"
            )
        user = super(UserCreationForm, self).save(commit=True)
        user.api_key = get_random_string(length=32)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    password2 = None

    class Meta:
        model = User
        fields = ("email",)
