from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
	judgeName = models.CharField(max_length=50, default = 'me')
	groupName = models.CharField(max_length=50)
	comment = models.TextField()
	techAcc = models.IntegerField()
	
	def __str__(self):
		return self.groupName	
