from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='teamuser', password='pass')
        url = reverse('team-list')
        data = {'name': 'Test Team', 'members': [user.id]}
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', password='pass')
        url = reverse('activity-list')
        data = {
            'user': user.id,
            'activity_type': 'Running',
            'duration': 30,
            'calories_burned': 300,
            'date': '2025-01-01'
        }
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {
            'name': 'Cardio Blast',
            'description': 'A high intensity cardio workout',
            'difficulty': 'Intermediate',
            'suggested_for': 'Weight Loss'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardEntryTests(APITestCase):
    def test_leaderboard_entry(self):
        user = User.objects.create_user(username='leaderuser', password='pass')
        entry = LeaderboardEntry.objects.create(user=user, total_calories=500, total_duration=60)
        self.assertEqual(str(entry), f"{user.username} - 500.0 cal")
