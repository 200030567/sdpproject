import random
import string

from django.http import HttpResponse


def hello(request):
    return HttpResponse("<center> Welcome to TTM</center>")


# Create your views here.


def newhomepage(request):
    return render(request, 'homepage.html')


def travelpackage(request):
    return render(request, 'travelpackage.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        a1 = {'user_input': user_input}
        return render(request, 'print_to_console.html', a1)


def randomcall(request):
    return render(request, 'randomotpgenerator.html')


def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))

    a1 = {'ran1': ran1}
    return render(request, 'randomotpgenerator.html', a1)


def getdate1(request):
    return render(request, 'get_date.html')


import datetime
from django.shortcuts import render
from .forms import *


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()
    return render(request, 'get_date.html', {'from': form})


from .models import *
from django.shortcuts import render, redirect


def myregisterpage(request):
    return render(request, 'Registration.html')


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Sowmya.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a different email.")
        Sowmya.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request, 'myregisterpage.html')


import matplotlib.pyplot as plt
import numpy as np


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')


def cars123(request):
    return render(request, 'cars123.html')


# views.py

from django.shortcuts import render
from django.http import HttpResponse
def weatherpagecall(request):
    return render(request, 'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        city = request.POST.get('place')
        # Logic to fetch weather data for the given city
        # For demonstration purposes, let's assume we have temperature and humidity data
        temperature1 = 25
        humidity = 60
        return render(request, 'your_template.html', {
            'city': city,
            'temperature1': temperature1,
            'humidity': humidity,
        })
    else:
        return render(request, 'your_template.html')
    

from django.shortcuts import render
from django. contrib.auth.models import User,auth
from django .contrib import messages
from django.contrib.auth.decorators  import login_required
def login(request):
    return render(request,'login.html')
def singup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'homepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'Homepage.html')




