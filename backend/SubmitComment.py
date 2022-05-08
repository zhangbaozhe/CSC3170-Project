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
                    SELECT `CommentID` 
                    FROM `Comments`
                    WHERE `UserID` = %s AND `CourseID` = %s;
                    """, [data["USERID"], data["COURSEID"]]
                )
                CommentID = cursor.fetchall()[0][0]
                print("Hello", CommentID)
                cursor.execute(
                    """
                    INSERT INTO `UsersGiveComments` (
                        `UserID`, `CommentID`
                    )
                    VALUES (
                        %s, %s
                    )
                    """, [data["USERID"], CommentID]
                )
                cursor.execute(
                    """
                    SELECT AVG(score) 
                    FROM `Comments`
                    WHERE `CourseID` = %s
                    GROUP BY `CourseID`
                    """, [data["COURSEID"]]
                )
                finalScore = float(cursor.fetchall()[0][0])
                print("Hello", finalScore)
                cursor.execute(
                    """
                    UPDATE `Courses`
                    SET `FinalScore` = %2.1f
                    WHERE `CourseID` = %s
                    """ %(finalScore, data["COURSEID"])
                )
                response = generate_response(None, 201)    
            return response
        return generate_response(None, 400)
    return generate_response(None, 400)