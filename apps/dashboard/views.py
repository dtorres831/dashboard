from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Messages, Posts
from ..userdashboard.models import User
# Create your views here.
def index(request):
    print User.objects.get(id=request.session['id'])
    print User.objects.all()
    context={
        "users": User.objects.all()
    }
    return render(request, "dashboard/users.html",context)
#admin start
def admin(request):
    context={
        "users": User.objects.all()
    }
    return render(request,"dashboard/admin.html", context)

def edit(request, id):
    context ={
        "user": User.objects.get(id=id)
    }
    return render(request, "dashboard/edit.html",context)

def updateinfo(request,id):
    print request.POST['user_level']
    if request.POST['user_level']=="admin":
        User.objects.filter(id=id).update(email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'], user_level=9)
        return redirect('dashboard:my_admin_home')
    else:
        User.objects.filter(id=id).update(email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'], user_level=1)
        return redirect('dashboard:my_admin_home')

def updatepass(request, id):
    response= User.objects.updatepass(request.POST)
    if not response['Status']:
        messages.error(request, response['errors'])
        return redirect('dashboard:my_edit',id=id)
    else:
        return redirect( 'dashboard:my_admin_home')
#admin ends
#user starts
def useredit(request, id):
    context={
        "user": User.objects.get(id=id)

    }
    return render(request, 'dashboard/useredit.html',context)
#end user edit
#user profile
def profile(request,id):
    # if request.method == 'POST':
    #     created_by = User.objects.get(id=request.session['id'])
    user = User.objects.get(id=id)
    # print Posts.objects.all()
    print '*'*100
    # print Posts.objects.all()

    #     Messages.objects.create(message=request.POST['message'], user=user, created_by=created_by)
    context ={
        "user": User.objects.get(id=id),
        "messages": Messages.objects.filter(user=user),
        "posts": Posts.objects.filter(created_by=User.objects.get(id=id))
    }

    return render(request, 'dashboard/profile.html', context)

def createmessage(request,id):
    if request.method == 'POST':
        created_by = User.objects.get(id=request.session['id'])
        user = User.objects.get(id=id)
        Messages.objects.create(message=request.POST['message'], user=user, created_by=created_by)
    return redirect('dashboard:my_profile', id=id)

def createpost(request,id):
    if request.method == 'POST':
        created_by = User.objects.get(id=id)
        user = User.objects.get(id=request.session['id'])
        Posts.objects.create(comment=request.POST['comment'], user=user, created_by=created_by)
    return redirect('dashboard:my_profile',id=id)

def userdes(request,id):
    User.objects.filter(id=id).update(description=request.POST['description'])
    return redirect('dashboard:my_home')
# def createmessage(request):
#     Messages.objects.create

#end user profie
def logout(request):
    del request.session['id']
    return redirect('home:my_home')
