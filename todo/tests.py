from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Todo

class TodoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_todo(self):
        url = reverse('todo-list')
        data = {'title': 'Test Todo', 'description': 'Test Description', 'due_date': '2023-12-31T23:59:59Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_todos(self):
        Todo.objects.create(user=self.user, title='Test Todo', description='Test Description', due_date='2023-12-31T23:59:59Z')
        url = reverse('todo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_todo(self):
        todo = Todo.objects.create(user=self.user, title='Test Todo', description='Test Description', due_date='2023-12-31T23:59:59Z')
        url = reverse('todo-detail', args=[todo.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        todo = Todo.objects.create(user=self.user, title='Test Todo', description='Test Description', due_date='2023-12-31T23:59:59Z')
        url = reverse('todo-detail', args=[todo.id])
        data = {'title': 'Updated Todo', 'description': 'Updated Description', 'due_date': '2023-12-31T23:59:59Z', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        todo = Todo.objects.create(user=self.user, title='Test Todo', description='Test Description', due_date='2023-12-31T23:59:59Z')
        url = reverse('todo-detail', args=[todo.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_todo_with_valid_due_date(self):
        url = reverse('todo-list')
        data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'due_date': (timezone.now() + datetime.timedelta(days=1)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_todo_with_past_due_date(self):
        url = reverse('todo-list')
        data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'due_date': (timezone.now() - datetime.timedelta(days=1)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('due_date', response.data)