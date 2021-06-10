from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import Group

# from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm

import requests

# @login_required(login_url='login')
# def userPage(request, pk_test):
# 	customer = Customer.objects.get(name=pk_test)
# 	# customer = request.user.customer.customer_set.all()
# 	# customer = request.customer.customer_set.all()
# 	context = {'customer': customer, }
# 	return render(request, 'NewsApp/index.html', context)

def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'NewsApp/account_settings.html', context)


def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			# this will automatically add new registered person to customer group which we have created using admin panel
			group = Group.objects.get(name='customer')
			user.groups.add(group)

			Customer.objects.create(
				user=user,
				name=user.username,
			)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form': form}
	return render(request, 'NewsApp/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'NewsApp/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

# def home(request):
# 	customers = Customer.objects.all()
#
# 	# total_customers = customers.count()
#
# 	context = {'customers':customers,}
#
# 	return render(request, 'NewsApp/dashboard.html', context)

# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)
#
# 	context = {'customer':customer,}
# 	return render(request, 'NewsApp/customer.html',context)



def index(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/index.html',{'top':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/index.html',{'top':general})


def general(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/general.html',{'general':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/general.html',{'general':general})


def music(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=music&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/music.html',{'music':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=music&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/music.html',{'music':general})

def sports(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=sports&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/sports.html',{'sports':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/sports.html',{'sports':general})


def entertainment(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=entertainment&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/entertainment.html',{'entertainment':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/entertainment.html',{'entertainment':general})


def technology(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=technology&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/technology.html',{'technology':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/technology.html',{'technology':general})


def science(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=science&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/science.html',{'science':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/science.html',{'science':general})


def politics(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=politics&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/politics.html',{'politics':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/politics.html',{'politics':general})


def health(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=health&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/health.html',{'health':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/health.html',{'health':general})


def business(request):
    if request.user.is_authenticated:
        data=Customer.objects.all()
        for i in data:
            if i.name==str(request.user.username):
                country=str(i.location)
                break
        general=requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&category=business&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/business.html',{'business':general})
    else:
        general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cbabce54cbcf40a29582d22d38332c4e').json()
        return render(request,'NewsApp/business.html',{'business':general})
