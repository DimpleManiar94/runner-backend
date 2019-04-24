from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import UserAccount, User
import requests

# Create your tests here.

client = APIClient()

class AccountTests(APITestCase):
    def test_create_account(self):
        data = { "user" : { "first_name" : "d", "last_name" : "xyz", "email" : "abcdfxyz@gmail.com", "username" : "d",
                            "password" : "runner123"
} }
        response = client.post('/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserAccount.objects.count(), 1)
        self.assertEqual(UserAccount.objects.get().user.username, 'd')
        print("Register response : ", response)

    def test_get_profile(self):
        user = User(first_name="c", last_name = "xyz", email="abcdfxyz@gmail.com", username="c", password="runner123")
        user.save()
        user = User.objects.get(username='c')
        client.force_authenticate(user=user)
        response = client.get('/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Profile response : ", response)

    def test_sign_in(self):
        url = "http://localhost:8000/api-token-auth/"
        payload = "{\n\t\"username\": \"c\",\n\t\"password\": \"runner123\"\n}"
        headers = {
            'Content-Type': "application/json",
        }
        user = User(first_name="c", last_name="xyz", email="abcdfxyz@gmail.com", username="c", password="runner123")
        user.save()
        response = requests.request("POST", url, data=payload, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Sign-In response : ", response)