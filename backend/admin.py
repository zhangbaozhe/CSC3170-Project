#from django.contrib import admin
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# from backend import serializers
# from backend.serializers import HelloWorldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Register your models here.

def generate_response(data, status):
    response = JsonResponse(data, safe=False, status = status)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
#allowed: delete,
def manage_user(request):
    with connection.cursor() as cursor:
        if(request.method == "DELETE"):
            try: 
                userID = request.data["data"]["id"]
            except:
                return generate_response(None, 400)
        return generate_response(None, 400)
#allowed: delete
#def manage_comment(request):

#allowed: add, delete
#def manage_course(request):
