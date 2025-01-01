from rest_framework.test import APIClient, APITestCase
from .models import CustomUser


# Testing user registration, login, logout
class TestUserManagment(APITestCase):
    def setUp(self):
        self.USERNAME = "sabi"
        self.PASSWORD = "tenco"
        self.REGISTER_URL = "/auth/register/"
        self.LOGIN_URL = "/auth/login/"
        self.LOGOUT_URL = "/auth/logout/"
        self.USERS_LIST_URL = "/users/all/"
        self.USER_INFO_URL = "/users/1/"
        self.USER_STATISTIC_URL = "/user/statistic/"
        self.client = APIClient()

    # User registration
    def test_user_registration(self):
        response = self.client.post(self.REGISTER_URL, data={
            "username": self.USERNAME,
            "password": self.PASSWORD
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 201)

    # Test user's uniqueness
    def test_user_uniqueness(self):
        CustomUser.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(self.REGISTER_URL, data={
            "username": self.USERNAME,
            "password": self.PASSWORD
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 226)

    # User login test
    def test_user_login(self):
        CustomUser.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(self.LOGIN_URL, data={
            "username": self.USERNAME,
            "password": self.PASSWORD
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 200)

    # User login testing without registration
    def test_not_registered_user_login(self):
        response = self.client.post(self.LOGIN_URL, data={
            "username": self.USERNAME,
            "password": self.PASSWORD
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 400)

    # User login test with wrong username
    def test_login_with_wrong_username(self):
        CustomUser.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(self.LOGIN_URL, data={
            "username": "None",
            "password": self.PASSWORD
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 400)

    # User login test with wrong password
    def test_login_with_wrong_password(self):
        CustomUser.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(self.LOGIN_URL, data={
            "username": self.USERNAME,
            "password": "None"
        })
        print(response.data["detail"])
        self.assertEqual(response.status_code, 400)

    # Logout test
    def test_logout(self):
        user = CustomUser.objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        self.client.force_authenticate(user)
        response = self.client.get(self.LOGOUT_URL)
        print(response.data["detail"])
        self.assertEqual(response.status_code, 200)

