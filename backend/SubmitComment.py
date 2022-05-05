from django.db import connection 
from django.http import JsonResponse
from rest_framework.decorators import api_view
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
@api_view(['GET', 'POST'])
def submit_comment(request):
    if (request.method == "POST"):
        data = request.data
        if data is not None: 
            print(data)
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO `Comments` (
                        `UserID`, `Year`, `Semester`, `Instructor`, `Score`, 
                        `Content`, `LikeNum`, `DislikeNum`, `CourseID`) 
                        VALUES (
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s)
                    """, [data["USERID"], data["YEAR"],data["SEMESTER"], \
                    data["INSTRUCTOR"],data["SCORE"],data["CONTENT"],data["LIKENUM"],data["DISLIKENUM"], data["COURSEID"]]
                )
                cursor.execute(
                    """
                    INSERT INTO `UsersGiveComments` (
                        `UserID`, `CommentID`
                    )
                    VALUES (
                        %s, %s
                    )
                    """, [data["USERID"], data["COMMENTID"]]
                )
                response = generate_response(None, 201)    
            return response
        return generate_response(None, 400)
    return generate_response(None, 400)