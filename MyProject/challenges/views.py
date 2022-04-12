from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("user setting")

def edit_profile(request):
    return HttpResponse("edite")
