from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from testapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# from django.views.generics import TemplateView
from django.core.files.storage import FileSystemStorage


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request ,'testapp/upload.html')


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['maheshpy85@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/testapp/sucess')

def sucess(request):
    return HttpResponse('Email Sent sucessfully')


def test(request):
    return HttpResponse('Testing app')

def testing(request):
    return render(request, 'testapp/test.html')

def index(request):
    return render(request,'testapp/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            # user_form.password.save()
            # user_form.email.save()
            user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['profile_pic']
            # profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    return render(request,'testapp/registration.html',
                          {'user_form':user_form,
                           # 'profile_form':profile_form,
                           'registered':registered})


# def register(request):
#     return HttpResponse('testing register url')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'testapp/login.html', {})

