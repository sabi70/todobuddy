from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Local imports
from .models import CustomUser
from .forms import CuctomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CuctomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "password"]


admin.site.register(CustomUser)
