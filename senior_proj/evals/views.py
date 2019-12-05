from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Session, TeamScore,GroupMember, SessionScore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from django.views.generic import ListView

#from .forms import UserRegisterForm
@login_required
def projEval(request):
    sessions= Session.objects.all()
    judgeName = 'judgeName' in request.POST and request.POST['judgeName']
    sessName = 'dropdown1' in request.POST and request.POST['dropdown1']
    grpName = 'dropdown2' in request.POST and request.POST['dropdown2']
    score1 = 'score1' in request.POST and request.POST['score1']
    score2 = 'score2' in request.POST and request.POST['score2']
    score3 = 'score3' in request.POST and request.POST['score3']
    score4 = 'score4' in request.POST and request.POST['score4']
    score5 = 'score5' in request.POST and request.POST['score5']
    score6 = 'score6' in request.POST and request.POST['score6']
    score7 = 'score7' in request.POST and request.POST['score7']
    score8 = 'score8' in request.POST and request.POST['score8']
    score9 = 'score9' in request.POST and request.POST['score9']
    score10 = 'score10' in request.POST and request.POST['score10']
    score11 = 'score11' in request.POST and request.POST['score11']
    score12 = 'score12' in request.POST and request.POST['score12']
    total = int(score1)+int(score2)+int(score3)+int(score4)+int(score5)+int(score6)+int(score7)+int(score8)+    int(score9)+int(score10)+int(score11)+int(score12)    
    proj_scores = TeamScore(teamName=grpName, sess=sessName, techAcc=score1, createIn=score2, analyt=score3,method=score4, complexit=score5, expect=score6, design=score7,quality=score8, organz=score9, time=score10, visAid=score11, confid=score12,total=total)
    proj_scores.save()
    return render(request, 'evals/projEval.html', {'title': 'Project Evaluation','sessions':sessions})

	#return render(request, 'evals/home.html') 

@login_required
def sessEval(request):
    judgeName = 'judgeName' in request.POST and request.POST['judgeName']
    disc = 'disc' in request.POST and request.POST['disc']
    score1 = 'score1' in request.POST and request.POST['score1']
    score2 = 'score2' in request.POST and request.POST['score2']
    score3 = 'score3' in request.POST and request.POST['score3']
    score4 = 'score4' in request.POST and request.POST['score4']
    score5 = 'score5' in request.POST and request.POST['score5']
    score6 = 'score6' in request.POST and request.POST['score6']
    score7 = 'score7' in request.POST and request.POST['score7']
    score8 = 'score8' in request.POST and request.POST['score8']
    score9 = 'score9' in request.POST and request.POST['score9']
    score10 = 'score10' in request.POST and request.POST['score10']
    score11 = 'score11' in request.POST and request.POST['score11']
    score12 = 'score12' in request.POST and request.POST['score12']	
    comment = 'comments' in request.POST and request.POST['comments']
    total = int(score1)+int(score2)+int(score3)+int(score4)+int(score5)+int(score6)+int(score7)+int(score8)+int(score9)+int(score10)+int(score11)+int(score12)
    sess_scores = SessionScore(discipline=disc, score1=score1,score2=score2, score3=score3,score4=score4, score5=score5, score6=score6, score7=score7,score8=score8, score9=score9, score10=score10, score11=score11, score12=score12,comments = comment,total=total)
    sess_scores.save()
    return render(request, 'evals/sessEval.html',{'title': 'Session Evaluation'})

#class SessionScoreTable(ListView):
  #  model = SessionScore
  #  template_name='evals/tabularResults.html'

def createSess(request):
	return render(request, 'evals/createSess.html', {'title': "Create Session"})

@login_required
def profile(request):
	return render(request, 'evals/profile.html')

# Create your views here.i
#def judgeLogin(request):
#	form = UserCreationForm()
#	return render(request, 'users/register
