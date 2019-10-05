"""Forms for user"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.crypto import get_random_string
from .models import User


class UserCreationWithoutUsernameForm(UserCreationForm):
    """User creation form class. Uses email instead of username and no password confirmation"""
    username = None
    password2 = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].help_text = "Min. 8 characters"

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save"
            )
        user = super().save(commit=True)
        user.api_key = get_random_string(length=32)
        user.save()
        return user

    class Meta:
        """Meta class for User"""
        model = User
        fields = ("email",)


class UserWithoutPassWordConfirmationChangeForm(UserChangeForm):
    """User change form. Uses email and no password confirmation"""
    password2 = None

    class Meta:
        """Meta class for user"""
        model = User
        fields = ("email",)
