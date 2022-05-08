from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# from backend import serializers
# from backend.serializers import HelloWorldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

def generate_response(data, status):
    response = JsonResponse(data, safe=False, status = status)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def like(request):
    with connection.cursor() as cursor:
        if(request.method == "POST"):
            try:
                userID = request.data["userID"]
                status = request.data["status"]
                commentID = request.data["commentID"]
                likeNum = request.data["likeNum"]
                dislikeNum = request.data["dislikeNum"]
            except:
                return generate_response(None, 400)
            cursor.execute(
                """
                INSERT INTO `CommentLikeStatus` 
                (`UserID`, `CommentID`, `Status`)
                VALUES
                (%s, %s, %s);
                """%(userID, commentID, status)
            )
            if(status == 1 or status == 2):
                cursor.execute(
                            """
                            UPDATE `Comments` 
                            SET `LikeNum` = %d, `DisLikeNum` = %d
                            WHERE `CommentID` = %s;
                            """%(likeNum,dislikeNum,commentID)
                        )
            #TODO: update `UsersSetCommentLikeStatus`?
            return generate_response(None, 201)
        elif(request.method == "PUT"):
            try:
                userID = str(request.data["userID"])
                status = str(request.data["status"])
                commentID = str(request.data["commentID"])
                likeNum = request.data["likeNum"]
                dislikeNum = request.data["dislikeNum"]
            except:
                return generate_response(None, 400)
            if(status=="0"):
                try:
                    cursor.execute(
                        """
                        DELETE FROM `CommentLikeStatus`
                        WHERE `UserID` = %s and `CommentID` = %s;
                        """%(userID, commentID)
                    )
                    cursor.execute(
                            """
                            UPDATE `Comments` 
                            SET `LikeNum` = %d, `DisLikeNum` = %d
                            WHERE `CommentID` = %s;
                            """%(likeNum,dislikeNum,commentID)
                    )
                except:
                    return generate_response(None,400)
            else:
                try:
                    cursor.execute(
                        """
                        UPDATE `CommentLikeStatus` 
                        SET `Status` = %s
                        WHERE `UserID` = %s and `CommentID` = %s;
                        """%(status, userID, commentID)
                    )
                    cursor.execute(
                            """
                            UPDATE `Comments` 
                            SET `LikeNum` = %d, `DisLikeNum` = %d
                            WHERE `CommentID` = %s;
                            """%(likeNum,dislikeNum,commentID)
                    )
                except:
                    return generate_response(None, 400)
            return generate_response(None, 204)

