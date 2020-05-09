from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from .models import History


class APITest(APITestCase):
  def set_credentials(self):
    url = '/api/api-token-auth/'
    data = {
      'username': self.username,
      'password': self.password
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
    return response.data['user_id']

  def setUp(self):
    self.username = 'testusername'
    self.email = 'test@gmail.com'
    self.password = 'testpassword'
    self.user = User.objects.create_user(self.username, self.email, self.password)

  def test_create_user(self):
    """
    Ensure we can create a new user object.
    """
    url = '/api/users/'
    data = {
      'username': 'newusername',
      'email': 'new@gmail.com',
      'password': 'newpassword'
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(User.objects.count(), 2)
    self.assertEqual(User.objects.get(username='newusername').email, 'new@gmail.com')

  def test_get_user_by_token(self):
    """
    Ensure we can get the user detail.
    """
    user_id = self.set_credentials()
    url = '/api/users/{user_id}/'.format(user_id=user_id)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_history(self):
    """
    Ensure we can add/get personalized user history.
    """
    # Add history for another user
    user2 = User.objects.create_user('username2', 'password2')
    History.objects.create(query='user2query', owner=user2)

    # Test add history
    queries = ["user1query1", "user1query2"]
    user_id = self.set_credentials()
    url = '/api/histories/'
    for query in queries:
      data = {
        "query": query
      }
      response = self.client.post(url, data)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(len(History.objects.filter(owner=user_id)), len(queries))

    # Test retrive histories
    url = '/api/users/{}/'.format(user_id)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['histories'], list(reversed(queries)))




  








