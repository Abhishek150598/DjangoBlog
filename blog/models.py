from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Profile(AbstractUser):
	date_of_birth = models.DateField(null=True)
	gender = models.CharField(max_length=10)
	bio = models.TextField(max_length=100, blank=True)

class Blog(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	title = models.CharField(max_length = 50)
	content = models.TextField(max_length = 500)
	created_date = models.DateTimeField(default = timezone.now)
	publish_date = models.DateTimeField(blank = True, null = True)

	def __str__(self):
		return self.title

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

