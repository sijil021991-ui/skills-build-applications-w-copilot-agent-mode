from djongo import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	class Meta:
		app_label = 'core'

class Activity(models.Model):
	user_email = models.EmailField()
	team = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()
	class Meta:
		app_label = 'core'

class Leaderboard(models.Model):
	team = models.CharField(max_length=100)
	points = models.IntegerField()
	class Meta:
		app_label = 'core'

class Workout(models.Model):
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
	class Meta:
		app_label = 'core'
from django.db import models

# Create your models here.
