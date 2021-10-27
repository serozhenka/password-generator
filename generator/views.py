from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get('length', 6))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend([letter.upper() for letter in characters])
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+"))
    if request.GET.get('numbers'):
        characters.extend(list("123456789"))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {"password": thepassword})
