from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{'hello': 'hello hometree11'})

def test(request):
    return HttpResponse("test hello")

