from django.urls import path
from . import views


urlpatterns = [
	path('', views.projEval,name='projEval'),
	path('sessEval/', views.sessEval,name='sessEval'),
	path('createSess/', views.createSess,name='createSess'),
	#path('tabularResults/', views.SessionScoreTable,name='SessionScoreTable'),
]
