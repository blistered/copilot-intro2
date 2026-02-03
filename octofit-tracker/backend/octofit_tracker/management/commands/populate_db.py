from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users
        users = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': 'Marvel'},
        ]
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {'name': 'Marvel', 'members': ['Iron Man', 'Captain America', 'Black Widow']},
            {'name': 'DC', 'members': ['Superman', 'Batman', 'Wonder Woman']},
        ]
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {'user': 'Superman', 'activity': 'Flight', 'duration': 60},
            {'user': 'Iron Man', 'activity': 'Suit Training', 'duration': 45},
        ]
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 150},
            {'team': 'DC', 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {'user': 'Batman', 'workout': 'Martial Arts', 'duration': 30},
            {'user': 'Black Widow', 'workout': 'Spy Training', 'duration': 40},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
