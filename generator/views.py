from django.shortcuts import render
import random
from string import ascii_lowercase, ascii_uppercase


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    alphabet_list = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        alphabet_list.extend(list(ascii_uppercase))

    if request.GET.get('special'):
        alphabet_list.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        alphabet_list.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(alphabet_list)

    return render(request, 'generator/password.html', {'password': thepassword})


def creator(request):
    return render(request, 'generator/creator_information.html')
