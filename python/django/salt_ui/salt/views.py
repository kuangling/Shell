# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
username='root'
def index(self):
    return HttpResponse('this is a django web')
def login(self,username='root'):
    return render_to_response('login.html',{'username':username})
