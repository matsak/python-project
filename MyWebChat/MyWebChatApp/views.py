from django.shortcuts import render

# Create your views here.
from MyWebChatApp import registration, login
from django.views.decorators.http import require_POST

@require_POST
def registration_in(request):
    return registration.registration_in(request)

@require_POST
def login_in(request):
    return login.login_in(request)