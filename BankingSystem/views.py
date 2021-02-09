from django.shortcuts import render
from django.http import HttpResponse
from .models import users
# Create your views here.
def index(request):
    return render(request,'index.html')

def user(request):
    return render(request,'members.html')

def transaction(request):
    return render(request,'transaction.html')

def history(request):
    return render(request,'history.html')

def register(request):
    if request.method == 'POST' :
        username = request.POST["username"]
        Mobile = request.POST["Mobile"]
        amount = request.POST["amount"]

        user = users(username = username , Mobile = Mobile , amount = amount)
        user.save()
        print("user created")
        return redirect('')
    else:
        return render(request, '')

