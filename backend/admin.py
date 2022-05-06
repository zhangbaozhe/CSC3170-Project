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
@csrf_exempt
@api_view(['DELETE'])
def manage_user(request):
    with connection.cursor() as cursor:
        if(request.method == "DELETE"):
            try: 
                userID = str(request.data["id"])
            except:
                return generate_response(None, 400)
            cursor.execute(
                f"""
                DELETE FROM `UsersGiveComments`
                WHERE `UserID` = {userID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `Comments`
                WHERE `UserID` = {userID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `CommentLikeStatusAppraiseComments`
                WHERE `UserID` = {userID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `CommentLikeStatus`
                WHERE `UserID` = {userID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `MultiComments`
                WHERE `UserID` = {userID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `Users`
                WHERE `UserID` = {userID};
                """
            )
            return generate_response(None, 204)


#allowed: delete
@csrf_exempt
@api_view(['DELETE'])
def manage_comment(request):
    with connection.cursor() as cursor:
        if(request.method == "DELETE"):
            try: 
                commentID = str(request.data["id"])
            except:
                return generate_response(None, 400)
            try:

                cursor.execute(
                    f"""
                    DELETE FROM `CommentLikeStatusAppraiseComments`
                    WHERE `CommentID` = {commentID};
                    """
                )
                cursor.execute(
                    f"""
                    DELETE FROM `CommentLikeStatus`
                    WHERE `CommentID` = {commentID};
                    """
                )
                cursor.execute(
                    f"""
                    DELETE FROM `UsersSetCommentLikeStatus`
                    WHERE `CommentID` = {commentID};
                    """
                )
                cursor.execute(
                    f"""
                    DELETE FROM `MultiComments`
                    WHERE `ParentCommentID` = {commentID};
                    """
                )
                cursor.execute(
                    f"""
                    DELETE FROM `MultiCommentsReplyComments`
                    WHERE `CommentID` = {commentID};
                    """
                )
                cursor.execute(
                    f"""
                    DELETE FROM `Comments`
                    WHERE `CommentID` = {commentID};
                    """
                )
            except:
                return generate_response(None, 400)
            return generate_response(None, 204)

#allowed: add, delete
@csrf_exempt
@api_view(['DELETE', 'POST'])
def manage_course(request):
    with connection.cursor() as cursor:
        if(request.method == "DELETE"):
            try: 
                courseID = str(request.data["id"])
            except:
                return generate_response(None, 400)


            cursor.execute(
                f"""
                DELETE FROM `Comments`
                WHERE `CourseID` = {courseID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `CommentsEvaluateCourses`
                WHERE `CourseID` = {courseID};
                """
            )
            cursor.execute(
                f"""
                DELETE FROM `Courses`
                WHERE `CourseID` = {courseID};
                """
            )
            return generate_response(None, 204)
        elif(request.method == "POST"):
            try: 
                courseName = request.data["CourseName"]
                school = request.data['School']
                credit = request.data["Credits"]
            except:
                return generate_response(None, 400)
            cursor.execute(
                f"""
                INSERT INTO `Courses` (
                    `CourseName`, `School`, `Credits`, `IsValid`, 
                    `FinalScore`) 
                    VALUES (
                    "{courseName}", "{school}", {credit}, 1, 0.0);
                """
            )
            return generate_response(None, 201)

@csrf_exempt
@api_view(['GET'])
def get_all(request):
    with connection.cursor() as cursor:
        tmp = {}
        tmp["Courses"] = []
        tmp["Users"] = []
        tmp["Comments"] = []
        cursor.execute(
            """
            SELECT `CourseID`, `CourseName` FROM `Courses`
            """
        )
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            tmp["Courses"].append(item)

        cursor.execute(
            """
            SELECT `CommentID`, `Content`, `UserID` FROM `Comments`
            """
        )
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            tmp["Comments"].append(item)
        
        cursor.execute(
            """
            SELECT `UserID`, `UserName` FROM `Users`
            """
        )
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            tmp["Users"].append(item)
        
        return generate_response(tmp, 200)