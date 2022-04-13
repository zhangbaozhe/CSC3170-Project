from django.shortcuts import render
from template import models
# Create your views here.

def orm(request):
    data_list = models.Users.objects.all()
    for users in data_list:
        print(users.User_ID)