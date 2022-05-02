from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# from backend import serializers
# from backend.serializers import HelloWorldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def hello_world(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS `messages` (
            `MSG_ID` INT(5) NOT NULL, 
            `MSG_CONTENT` VARCHAR(20), 
            PRIMARY KEY (`MSG_ID`));
            """
        )

        if request.method == 'GET':
            cursor.execute(
                """
                SELECT * FROM `messages`;
                """
            )
            columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            # print(data)
            response = JsonResponse(data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif request.method == 'POST':
            cursor.execute(
                """
                SELECT * FROM `messages`;
                """
            )
            print(request.data)
            if request.data is not None:
                de_data = request.data
                print(de_data)
                cursor.execute(
                    """
                   INSERT INTO `messages` (`MSG_ID`, `MSG_CONTENT`)
                   VALUES (%s, %s); 
                    """, [de_data['MSG_ID'], de_data['MSG_CONTENT']]
                )
                response = JsonResponse(de_data, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "*"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "*"
                return response
            response = JsonResponse(de_data, status=status.HTTP_400_BAD_REQUEST)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
            
def course(request):
    with connection.cursor() as cursor:

        if request.method == 'GET':
            cursor.execute(
                """
                SELECT * 
                FROM `Comments`,`users`
                where comments.userid = users.userid;
                """
            )
            columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            # print(data)
            response = JsonResponse(data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif request.method == 'POST':
            cursor.execute(
                """
                SELECT * FROM `messages`;
                """
            )
            print(request.data)
            if request.data is not None:
                de_data = request.data
                print(de_data)
                cursor.execute(
                    """
                   INSERT INTO `messages` (`MSG_ID`, `MSG_CONTENT`)
                   VALUES (%s, %s); 
                    """, [de_data['MSG_ID'], de_data['MSG_CONTENT']]
                )
                response = JsonResponse(de_data, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "*"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "*"
                return response
            response = JsonResponse(de_data, status=status.HTTP_400_BAD_REQUEST)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

    # messages = { 'msg_id' : 1, 'msg_content' : "Hello, world"}
    # serializer = HelloWorldSerializer(messages)
    # if request.method == 'GET':

    # return JsonResponse(serializer.data, safe=False)
