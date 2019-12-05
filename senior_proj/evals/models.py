from django.db import models
from django import forms
from django.contrib.auth.models import User


#class Post(models.Model):
	#judgeName = models.CharField(max_length=50, default = 'me')
	#groupName = models.CharField(max_length=50)
	#comment = models.TextField()
	#techAcc = models.IntegerField()
	#def __str__(self):
		#return self.groupName

class TeamScore(models.Model):
    teamName = models.CharField(max_length=20,default='NA')
    sess = models.CharField(max_length=50,default='NA')
    judgeName = models.CharField(max_length=20,default='NA')
    techAcc = models.IntegerField()
    createIn = models.IntegerField()
    analyt = models.IntegerField()
    method = models.IntegerField()
    complexit = models.IntegerField()
    expect = models.IntegerField()
    design = models.IntegerField()
    quality = models.IntegerField()
    organz = models.IntegerField()
    time = models.IntegerField()
    visAid = models.IntegerField()
    confid = models.IntegerField()
    total = models.IntegerField()
    def __str__(self):
        return self.teamName


#class Judge(models.Model):
class SessionScore(models.Model):
    judgeName = models.CharField(max_length=20,default='NA')
    discipline = models.CharField(max_length=50,default='NA')
    score1 = models.IntegerField()
    score2= models.IntegerField()
    score3= models.IntegerField()
    score4= models.IntegerField()
    score5= models.IntegerField()
    score6= models.IntegerField()
    score7= models.IntegerField()
    score8= models.IntegerField()
    score9= models.IntegerField()
    score10= models.IntegerField()
    score11= models.IntegerField()
    score12= models.IntegerField()
    total = models.IntegerField()
    comments = models.TextField()
    def __str__(self):
        return self.discipline

class GroupMember(models.Model):
    groupName = models.CharField(max_length=50,default='NA')
    Student1 = models.CharField(max_length=50,default='NA')
    Student2 = models.CharField(max_length=50,default='NA')
    Student3 = models.CharField(max_length=50,default='NA')
    Student4 = models.CharField(max_length=50,default='NA')
    def __str__(self):
        return self.groupName


class Session(models.Model):
    dept=(
		('Electical Engineering', "Electrical Engineering"),
		('Computer Engineering', "Computer Engineering"),
		('Mechanical Engineering', "Mechanical Engineering"))
    session_Name = models.CharField(max_length= 30, choices =dept) 
    judge1 = models.CharField(max_length=50,default='NA')	
    judge2 = models.CharField(max_length=50,default='NA')
    judge3 = models.CharField(max_length=50,default='NA')
    judge4 = models.CharField(max_length=50,default='NA')
    judge5 = models.CharField(max_length=50,default='NA')
    
    group1 = models.CharField(max_length=50, default='NA')
    group2 = models.CharField(max_length=50,default='NA')
    group3 = models.CharField(max_length=50,default='NA')
    group4 = models.CharField(max_length=50,default='NA')
    group5 = models.CharField(max_length=50,default='NA')
    group6 = models.CharField(max_length=50,default='NA')
    group7 = models.CharField(max_length=50,default='NA')
    group8 = models.CharField(max_length=50,default='NA')
    group9 = models.CharField(max_length=50,default='NA')
    group10 = models.CharField(max_length=50,default='NA')

    def __str__(self):
        return self.session_Name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'	
