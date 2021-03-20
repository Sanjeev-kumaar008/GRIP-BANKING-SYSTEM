from django.db import models


# Create your models here.
class users(models.Model) :
    username = models.CharField(max_length = 100)
    amount = models.IntegerField()
    mobile = models.BigIntegerField()
    transferedTo = models.CharField(max_length = 100)
    amountAdd = models.CharField(max_length = 100)
    
    
    
    
    
    
    
   
    

