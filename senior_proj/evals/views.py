from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
def projEval(request):
	return render(request, 'evals/projEval.html', {'title': 'Project Evaluation'})
	#return render(request, 'evals/home.html') 

def sessEval(request):
	return render(request, 'evals/sessEval.html',{'title': 'Session Evaluation'})

def createSess(request):
	return render(request, 'evals/createSess.html', {'title': "Create Session"})

def profile(request):
	return render(request, 'evals/profile.html')

# Create your views here.i
#def judgeLogin(request):
#	form = UserCreationForm()
#	return render(request, 'users/register
