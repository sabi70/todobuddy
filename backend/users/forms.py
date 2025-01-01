from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ValidationError

from .models import CustomUser


class CuctomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ["username", "password"]

