from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=15)
    completed = models.IntegerField(default=0)
    not_completed = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return f"{self.username} {self.password}"

