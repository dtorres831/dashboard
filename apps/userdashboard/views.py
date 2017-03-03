from django.shortcuts import render,redirect
from django.contrib import messages

from .models import User

# Create your views here.
def index(request):
    return render(request, "userdashboard/index.html")

def signin(request):
    return render(request,"userdashboard/signin.html")

def vsignin(request):


    response = User.objects.login(request.POST)
    # print response['user'].user_level
    if not response['Status']:
        messages.error(request, response['errors'])
        return redirect('home:my_signin')
    else:
        if response['user'].user_level == 9:
            print '*'*100
            request.session['id']= response['user'].id
            return redirect('dashboard:my_admin_home')


        else:
            request.session['id']= response['user'].id
            return redirect( 'dashboard:my_home')

def register (request):
    return render(request,"userdashboard/register.html")

def vregister(request):
    response = User.objects.register(request.POST)
    if not response['Status']:
        for error in response['errors']:
            messages.error(request, error)
            print response['errors']
        return redirect('home:my_register')
    else:
        if response['user'].user_level == 9:
            request.session['id']= response['user'].id
            return redirect('dashboard:my_admin_home')
        else:
            request.session['id']= response['user'].id
            return redirect( 'dashboard:my_home')
