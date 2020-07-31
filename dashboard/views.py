# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, PassChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Upload Data

def Dashboard(request):
	return render(request,'dashboard/dash.html',{})

def Census(request):
     return render(request,'dashboard/census.html',{})


def DP_2014_34(request):
     return render(request,'dashboard/dp_2014_34.html',{})

def SWM(request):
    return render(request,'dashboard/solidwastemanagement.html')

def palgarh(request):
    return render(request,'dashboard/d3_palgarh_double_slider.html')
	

def Goadashboards(request):
    return render(request,'dashboard/goa_maps.html')
	
def IITBombay(request):
    return render(request,'dashboard/iit.html',{})    


def Education(request):
    return render(request,'dashboard/education.html')

def Test(request):
    if request.method == 'POST':
        FORM = lA
    return render(request,'dashboard/test.html')  

def Transport(request):
    return render(request,'dashboard/transportation.html')


def Health(request):
    context = {'site_url':settings.MY_SITE_URL}
    return render(request,'dashboard/health.html',context)

def UrbanHealth(request):
    return render(request,'dashboard/town_health.html')

def Water(request):
    return render(request,'dashboard/ruralwater.html')

def tdsc(request):
    return render(request,'dashboard/tdsc.html')

@login_required
def melghat(request):
    return render(request,'dashboard/melghat.html')

def ahmadnagargis(request):
    return render(request,'dashboard/ahmadnagar.html')

@login_required
def tdd(request):
    return render(request,'dashboard/tdd.html')


def test_animesh(request):

    theme_name = "Deonadi Project Dashboard"
    options = {'1':'Deonadi Watershed Villages',
                '2':'Deonadi Watershed Drainage',
                '3':'Deonadi Watershed Wells',
                '4':'Deonadi Watershed Landuse 2005-06',
                '5':'Deonadi Watershed Landuse 2011-12',
                '6':'Deonadi Watershed Soil Depth',
                '7':'Deonadi Watershed contour line',
                '8':'Please Select layers'
               }
    context = {'site_url':settings.MY_SITE_URL,'opt':options}
    return render(request,'dashboard/test.html',context)

def tby(request):
    return render(request,'dashboard/tby.html')


def deonadi(request):
    theme_name = "Deonadi Project Dashboard"
    options = {'1':'Deonadi Watershed Villages',
                '2':'Deonadi Watershed Drainage',
                '3':'Deonadi Watershed Wells',
                '4':'Deonadi Watershed Landuse 2005-06',
                '5':'Deonadi Watershed Landuse 2011-12',
                '6':'Deonadi Watershed Soil Depth',
                '7':'Deonadi Watershed contour line',
                '8':'Please Select layers'
               }
    return render(request,'dashboard/tnc.html',{'title': theme_name,'options':options})

def pwss(request):
    return render(request,'dashboard/pwss.html')

def covidLive(request):
    return render(request,'dashboard/covid_live.html')

# def front(request):
# 	return render(request,'map/front.html')

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request,('Successfully loged in'))
#             return redirect('home')
#         else:
#             messages.success(request,('Please try again!'))
#             return redirect('login')
#     else:
#         return render(request,'map/login.html',{})

# def signup_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'map/signup.html', {'form': form})


# def logout_user(request):
#     logout(request)
#     messages.success(request,('logged out!!'))
#     return render(request,'map/front.html',{})

# def change_password(request):
#     if request.method == 'POST':
#         form = PassChangeForm(data = request.POST, user = request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request,form.user)
#             messages.success(request, 'Your password is successfully updated!')
#             return redirect('home')
#     else:
#         form = PassChangeForm(user = request.user) 
#     return render(request,'map/changepassword.html',{'form': form})


# def demo(request):
#     return render(request,'map/demo.html')




# def upload_layers(request):
#     if request.method == 'POST':
#         form = LayersForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = form.save(commit=False)
#             file.user = request.user
#             file.save()
#             messages.success(request, 'Your file is saved')
#             return redirect('show_upload')
#     else:
#         form = LayersForm()
#     return render(request,'map/upload_layers.html',{'form':form})


# def show_upload(request):
#     layers = Layers.objects.filter(user_id = request.user.id)
#     if not layers:
#         messages.success(request,'No Layer found')
#     return render(request,'map/showupload.html',{'layers':layers})

# def show_all_upload(request):
#     alllayers = Layers.objects.all()
#     if not alllayers:
#         messages.success(request,'No Layers Found')
#     return render(request,'map/showallupload.html',{'alllayers':alllayers})

# def delete_upload(request,pk):
#     if request.method == 'POST':
#         layer = Layers.objects.get(pk=pk)
#         layer.delete()
#     return redirect('show_upload')
