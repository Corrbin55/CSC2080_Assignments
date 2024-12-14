from django.shortcuts import render
from random import choice
import string

def home(request):
    items = ['Python', 'Django', 'JavaScript', 'Data Analysis', 'Machine Learning']
    return render(request, 'portfolio/home.html', {'items': items})

def generate_password(request):
    length = 12
    password = ''.join(choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return render(request, 'portfolio/password.html', {'password': password})
