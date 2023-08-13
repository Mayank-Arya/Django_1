from django.shortcuts import render

# Create your views here.

def welcome(req):
    return render(req, 'Welcome.html')

def greetUser(req, username):
    return render(req, 'greet.html', {'username':username})

def farewellUser(req,username):
    return render(req, 'farewell.html', {'username':username})