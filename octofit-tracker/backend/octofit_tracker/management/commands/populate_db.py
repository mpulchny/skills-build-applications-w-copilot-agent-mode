from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define sample data
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]
TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]
ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flying", "duration": 120},
    {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 90},
    {"user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 60},
]
LEADERBOARD = [
    {"team": "Marvel", "points": 180},
    {"team": "DC", "points": 210},
]
WORKOUTS = [
    {"name": "Strength Training", "difficulty": "Medium"},
    {"name": "Cardio Blast", "difficulty": "Hard"},
]

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
