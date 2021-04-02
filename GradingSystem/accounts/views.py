from django.shortcuts import render
from django.http import HttpResponse
from .models import smisformsdb
from .forms import smis_register, smis_forms

import re
from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users,admin_only
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.contrib.auth.decorators import permission_required


# Create your views here.

@unauthenticated_user
def smislogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('smishome')
        else:
            messages.info(request, 'Username Entered Could be Wrong: ' +username)
            messages.info(request, 'Password Entered Could be Wrong: ' +password)

    context = {}
    return render(request, 'accounts/authentication/loginform.html', context);

#Registration
@login_required(login_url='smislogin')
@admin_only
def smisregister(request):
    form = smis_register(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

            messages.success(request, 'Account Created Successfully for ' + username)
            return redirect('smisregister')
    context = {'form': form,}
    return render(request, 'accounts/authentication/registrationform.html', context);

#LogOut
def LogOut(request):
    logout(request)
    return redirect('smislogin')


#DeleteUser
@login_required(login_url='smislogin')
@admin_only
def delete_user(request, username):
    context = {}
    
    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = 'The user is deleted.'       
    except User.DoesNotExist: 
        context['msg'] = 'User does not exist.'
    except Exception as e: 
        context['msg'] = e.message

    return render(request, 'accounts/home/index.html', context=context)

def smisprofile(request):
    return render(request, 'accounts/authentication/profile.html')

@login_required(login_url='smislogin')
def smishome(request):
    return render(request, 'accounts/home/index.html');

def smisforms(request):
    if request.method == 'POST':
        form = smis_forms(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'accounts/reports/results.html')

    else:
        form = smis_forms(request.POST)
        context = {'form':form,}
        return render(request, 'accounts/userforms/gradesforms.html',context)


def smisresults(request):
    context = {'smisresults': smisformsdb.objects.all()}
    return render(request, 'accounts/reports/results.html', context);

def smistranscript(request):
    context = {'smistranscript': smisformsdb.objects.all()}
    return render(request, 'accounts/reports/transcript.html', context);