from django.urls import path, re_path

from .views import RegisterView, LoginView, LogoutView, UsersListView, StatisticUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    re_path(r"^users/(?P<data>\w+)/?$", UsersListView.as_view()),
    path("user/statistic/", StatisticUpdateView.as_view()),
]

