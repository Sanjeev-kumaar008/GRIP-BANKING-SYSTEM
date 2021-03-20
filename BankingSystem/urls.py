from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name = 'index'),
    path('members',views.user,name = 'members'),
    path('transaction',views.transfer,name = 'transaction'),
    path('history',views.history,name = 'history'),

    
]