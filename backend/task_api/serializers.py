from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = ["author", "title", "done", "creation_date", "pk"]
        read_only_fields = ["author"]

