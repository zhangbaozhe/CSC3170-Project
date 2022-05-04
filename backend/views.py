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
def generate_response(data, status):
    response = JsonResponse(data, safe=False, status = status)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

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
            # response = JsonResponse(data, safe=False)
            # response["Access-Control-Allow-Origin"] = "*"
            # response["Access-Control-Allow-Methods"] = "*"
            # response["Access-Control-Max-Age"] = "1000"
            # response["Access-Control-Allow-Headers"] = "*"
            return generate_response(data, 200)
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
                # response = JsonResponse(de_data, status=status.HTTP_201_CREATED)
                # response["Access-Control-Allow-Origin"] = "*"
                # response["Access-Control-Allow-Methods"] = "*"
                # response["Access-Control-Max-Age"] = "1000"
                # response["Access-Control-Allow-Headers"] = "*"
                return generate_response(de_data, 201)
            # response = JsonResponse(de_data, status=status.HTTP_400_BAD_REQUEST)
            # response["Access-Control-Allow-Origin"] = "*"
            # response["Access-Control-Allow-Methods"] = "*"
            # response["Access-Control-Max-Age"] = "1000"
            # response["Access-Control-Allow-Headers"] = "*"
            return generate_response(de_data, 400)
            
def course(request):
    with connection.cursor() as cursor:

        if request.method == 'GET':
            courseid = request.GET.get("courseID")
            cursor.execute(
                """
                SELECT * ,Comments.content AS C, Mul.UserID AS MUserID, MUL.UserName AS MUserName
                FROM `Comments`,`users`,
                (select *
                from `MultiComments`,Users
                where MultiComments.userid = users.userid) AS Mul
                where (comments.userid = users.userid) and (Comments.CommentID = Mul.ParentCommentID);
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

@csrf_exempt
@api_view(['GET', 'POST'])
def login(request):
    with connection.cursor() as cursor:
        if(request.method == "GET"):
            try:
                username = request.GET.get("username")
                password = request.GET.get("password")
                print(username, "  ", password)
            except:
                return JsonResponse(status = 400)
            print("""
                SELECT * FROM `Users`
                WHERE `Username` = '%s' and `Password` = '%s';
                """%(username, password))
            
            cursor.execute(
                """
                SELECT * FROM `Users`
                WHERE `Username` = '%s' and `Password` = '%s';
                """%(username, password)
            )
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            if(len(data) == 0):
                print("no")
                return generate_response({'messages': 'username or password is incorrect', 'status': 'failed'}, 400)
            if(len(data) == 1):
                print("yes")
                userID = data[0]["UserID"]
                return generate_response({'messages': 'login success', 'status':'success', 'userID':userID}, 200)
    return generate_response({'messages': 'login failed', 'status':'failed'}, 400)

        
@csrf_exempt
@api_view(['GET', 'POST'])
def register_user(request):
    """Register a user
    """
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO `Users` 
                (`Username`, `Password`)
                VALUES
                (%s, %s)
                """, [request.data['USERNAME'], request.data['PASSWORD']]
            )
            # response = JsonResponse(request.data, status=status.HTTP_201_CREATED)
            # response["Access-Control-Allow-Origin"] = "*"
            # response["Access-Control-Allow-Methods"] = "*"
            # response["Access-Control-Max-Age"] = "1000"
            # response["Access-Control-Allow-Headers"] = "*"
            return generate_response(request.data, 201)
    # response = JsonResponse(None, status=status.HTTP_400_BAD_REQUEST)
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "*"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    return generate_response(None, 400)
    
    
@csrf_exempt
@api_view(['GET', 'POST'])
def get_users(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT `Username` FROM `Users`
                """
            )
            columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            print(data)
            # response = JsonResponse(data, safe=False)
            # response["Access-Control-Allow-Origin"] = "*"
            # response["Access-Control-Allow-Methods"] = "*"
            # response["Access-Control-Max-Age"] = "1000"
            # response["Access-Control-Allow-Headers"] = "*"
            return generate_response(data, 200)
    # response = JsonResponse(None, status=status.HTTP_400_BAD_REQUEST)
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "*"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    return generate_response(None, 400)

@csrf_exempt
@api_view(['GET', 'POST'])
def search(request):
    with connection.cursor() as cursor:

        if request.method == 'GET':
            cursor.execute(
                """
                SELECT *
                FROM `courses` as c1,
                (SELECT COUNT(*) as count, AVG(comments.score) as a, courses.courseid
                FROM `courses`,`comments`
                where courses.courseid = comments.courseid
                group by courses.courseid) as c
                where c1.courseid = c.courseid;
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


@csrf_exempt
@api_view(['GET', 'POST'])
def search_0(request):
    with connection.cursor() as cursor:

        if request.method == 'GET':
            cursor.execute(
                """
                SELECT *
                FROM `courses` 
                where courses.courseid not in 
                (SELECT courseid FROM comments);
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

@csrf_exempt
@api_view(['GET', 'POST'])
def search_1(request):
    Department = request.GET.get('Department')

    with connection.cursor() as cursor:

        if request.method == 'GET':
            if Department == 'all':
                cursor.execute(
                """
                SELECT *
                FROM `courses` as c1,
                (SELECT COUNT(*) as count, AVG(comments.score) as a, courses.courseid
                FROM `courses`,`comments`
                where courses.courseid = comments.courseid
                group by courses.courseid) as c
                where c1.courseid = c.courseid;
                """
            )
            else:
                cursor.execute(
                    f"""
                    SELECT *
                    FROM `courses` as c1,
                    (SELECT COUNT(*) as count, AVG(comments.score) as a, courses.courseid
                    FROM `courses`,`comments`
                    where courses.courseid = comments.courseid
                    group by courses.courseid) as c
                    where c1.courseid = c.courseid
                    and c1.school = '{Department}';
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

@csrf_exempt
@api_view(['GET', 'POST'])
def search_2(request):
    Department = request.GET.get('Department')

    with connection.cursor() as cursor:

        if request.method == 'GET':
            if Department == 'all':
                cursor.execute(
                """
                SELECT *
                FROM `courses` 
                where courses.courseid not in 
                (SELECT courseid FROM comments);
                """
            )
            else:
                cursor.execute(
                    f"""
                  SELECT *
                    FROM `courses` 
                 where courses.courseid not in 
                (SELECT courseid FROM comments)
                    and courses.school = '{Department}';
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