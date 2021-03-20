from django.shortcuts import render,redirect
from .models import users

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        amount = request.POST["amount"]
        mobile = request.POST["mobile"]

        user = users(username = username , mobile = mobile , amount = amount)
        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request,'register.html')



