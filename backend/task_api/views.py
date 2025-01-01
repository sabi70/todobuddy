from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication

from .models import Task
from .serializers import TaskSerializer


# Task view for next methods: get, post, update, delete
# Requires authentication for Task data managment
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
