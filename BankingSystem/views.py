from django.shortcuts import render
from django.http import HttpResponse
from registration.models import users

# Create your views here.
def index(request):
    return render(request,'index.html')

def user(request):
    user = users.objects.all()
    return render(request,'members.html',{'user':user})

def transfer(request):
    user = users.objects.all()
    if request.method == "POST":
        username1 = request.POST["username1"]
        username2 = request.POST["username2"]
        

        amountAdded = int(request.POST["amountAdded"])
        amtadd = request.POST["amountAdded"]
        
        
        user1 = users.objects.get(pk = username1)
        user1.amount = user1.amount - amountAdded
        
        user2 = users.objects.get(pk = username2)
        user2.amount = user2.amount + amountAdded
        user1.transferedTo = user1.transferedTo + user2.username 
        user1.amountAdd = user1.amountAdd + amtadd +"\n"
        
        
        
        user1.save()
        user2.save()
        
        
        
        
        print(user1.transferedTo,'\n')
        print(user1.amount)
        print(user2.amount)
        print(request.POST)

    return render(request,'transaction.html',{'user' : user})
   

def history(request):
    user = users.objects.all() 

    return render(request,'history.html',{'user' : user})


