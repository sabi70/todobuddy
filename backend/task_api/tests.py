from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model

from .models import Task


# ! All of your test cases must begin with word "test"
# Testing my task_api application for methods get, post, put, delete
class TestTaskApi(APITestCase):

    # initializing the client, user and task model
    def setUp(self):
        self.USERNAME = "sabi"
        self.PASSWORD = "tenco"
        self.TITLE = "Complete this App"
        self.URL = "/tasks/"
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username=self.USERNAME, password=self.PASSWORD)
        self.task = Task.objects.create(author=self.user, title=self.TITLE, done=False)

    # testing the get method with authentication
    def test_get_task_method_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
       
    # testing the get method without authentication
    def test_get_task_method_unauthenticated(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 401)
    
    # testing the post method with authentication
    def test_create_task_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(self.URL, data={"title": self.TITLE})
        self.assertEqual(response.status_code, 201)
        
    # testing the post method without authentication
    def test_create_task_unauthenticated(self):
        response = self.client.post(self.URL, data={"title": self.TITLE})
        self.assertEqual(response.status_code, 401)
    
    # testing the put method with authentication
    def test_put_task_authenticated(self):
        pk = self.task.pk
        URL = f"{self.URL}{pk}/"
        title = "New Title"
        self.client.force_authenticate(self.user)
        response = self.client.put(URL, data={"title": title})
        self.assertEqual(response.status_code, 200)
        
    # testing the put method without authentication        
    def test_put_task_unauthenticated(self):
        pk = self.task.pk
        URL = f"{self.URL}{pk}/"
        title = "New Title"
        response = self.client.put(URL, data={"title": title})
        self.assertEqual(response.status_code, 401)        
        
    # testing the delete method with authentication
    def test_delete_task_authenticated(self):
        pk = self.task.pk
        URL = f"{self.URL}{pk}/"
        self.client.force_authenticate(self.user)
        response = self.client.delete(URL)
        self.assertEqual(response.status_code, 204)
        
    # testing the delete method without authentication
    def test_delete_task_unauthenticated(self):
        task_pk = self.task.pk
        URL = f"{self.URL}{task_pk}/"
        response = self.client.delete(URL)
        self.assertEqual(response.status_code, 401)
