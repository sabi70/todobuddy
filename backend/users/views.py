from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.core import serializers

from .models import CustomUser
from .serializers import CustomUserSerializer, UserDataSerializer

from task_api.models import Task
from task_api.serializers import TaskSerializer

# User creation view
class RegisterView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        if CustomUser.objects.filter(username=username).exists():
            return Response({"detail": "User with this name already exists!"}, status=status.HTTP_226_IM_USED)
        user = CustomUser.objects.create_user(username=username, password=password)
        user.save()
        return Response({"detail": "You were successfuly registered"}, status=status.HTTP_201_CREATED)


# User login view
class LoginView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        if CustomUser.objects.filter(username=username).exists():            
            user = authenticate(request, username=username, password=password)
            if user is None:
                return Response({"detail": "The password is incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                login(request, user)
                return Response({
                    "detail": "You were successful logged in!",
                }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "This user does not exist!"}, status=status.HTTP_400_BAD_REQUEST)


# User logout view
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"detail": "You were successful logged-out!"}, status=status.HTTP_200_OK)


# Users list view for listing all usernames or one ordinary user's information
class UsersListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all().order_by("username")
    serializer_class = UserDataSerializer
    
    def get(self, request, data):
        try:
            int(data)
            user = CustomUser.objects.get(pk=data)
            user_serializer = UserDataSerializer(user)
            task = Task.objects.filter(author=user.pk)
            task_serializer = TaskSerializer(task, many=True)
            return Response(status=status.HTTP_200_OK, data={
                "user": user_serializer.data,
                "tasks": task_serializer.data
            })
        except ValueError:
            users = CustomUser.objects.all()
            serializer = UserDataSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


# Update view for user's completed or not_completed count information
class StatisticUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def update(self, request):
        user = CustomUser.objects.get(username=request.user.username)
        if request.data["completed"] == True:
            user.completed += 1
        else:
            user.not_completed += 1
        user.save()
        return Response({"detail": "The operation was successful!"}, status=status.HTTP_200_OK)

