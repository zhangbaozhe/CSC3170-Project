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
            
def append_course_info(tmp, course_id):
    with connection.cursor() as cursor:
        tmp["CommentedUsers"] = []
        cursor.execute(
            """
            SELECT `UserID`
            FROM `Comments` 
            WHERE `CourseID`=%s;
            """%course_id
        )
        columns = [col[0] for col in cursor.description]
        # data is a list TODO: caution! when converting to the JSON
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            tmp["CommentedUsers"].append(item["UserID"])
        cursor.execute(
            """
            SELECT  `CommentID`, u.`UserID`, `UserName`, `CourseID`, 
                    `Semester`, `Year`, `Instructor`, 
                    `Score`, `Content`, `LikeNum`, `DislikeNum`
            FROM `Comments` c, `Users` u
            WHERE `CourseID`=%s and u.`UserID` = c.UserID;
            """%course_id
        )
        columns = [col[0] for col in cursor.description]
        # data is a list TODO: caution! when converting to the JSON
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            cursor.execute(
                """
                SELECT * 
                FROM `CommentLikeStatus`
                WHERE `CommentID`=%s;
                """% str(item["CommentID"])
            )
            _columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            _data = [dict(zip(_columns, row)) for row in cursor.fetchall()]

            likeList = []
            dislikeList = []
            for _item in _data:
                if(_item["Status"] == 1):   # 0 = nostatus; 1 = like; 2 = dislike
                    likeList.append(_item["UserID"])
                elif(_item["Status"] == 2):
                    dislikeList.append(_item["UserID"])
            item["likeList"] = likeList
            item["dislikeList"] = dislikeList

        tmp["Comments"] = data
    return tmp
        

def course(request):
    with connection.cursor() as cursor:

        if request.method == 'GET':
            print(request.GET.get("courseID"))
            try:
                courseid = str(request.GET.get("courseID"))
            except:
                return generate_response(None, 400)
            try:
                cursor.execute(
                    """
                    SELECT * FROM `Courses`
                    WHERE `CourseID` = %s;
                    """%courseid
                )
            except:
                return generate_response(None, 400)
            columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            if(len(data) == 0):
                return generate_response(None, 400)
            tmp = data[0]
            tmp = append_course_info(tmp, courseid)

            response = JsonResponse(tmp, safe=False)
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
                (SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
                FROM `courses`,`comments`
                where courses.courseid = comments.courseid
                group by courses.courseid) as c
                where c1.courseid = c.courseid;
                """
            )
            columns = [col[0] for col in cursor.description]
            # data is a list TODO: caution! when converting to the JSON
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

            print("In search", data)
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
    Subject = request.GET.get('Subject')
    Content = request.GET.get('SearchContent')
    if Subject == 'all':
        Subject = ''
    if Department == '':
        Department = 'all'
    with connection.cursor() as cursor:

        if request.method == 'GET':
            if Department == 'all':
                cursor.execute(
                f"""
                SELECT *
                FROM `courses` as c1,
                (SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
                FROM `courses`,`comments`
                where courses.courseid = comments.courseid
                group by courses.courseid) as c
                where c1.courseid = c.courseid
                and c1.coursename like '{Subject}%'
                and (c1.coursename like '%{Content}%'
                or c1.school like '%{Content}%');
                """
            )
            else:
                cursor.execute(
                    f"""
                    SELECT *
                    FROM `courses` as c1,
                    (SELECT COUNT(*) as count, ROUND(AVG(comments.score),1) as a, courses.courseid
                    FROM `courses`,`comments`
                    where courses.courseid = comments.courseid
                    group by courses.courseid) as c
                    where c1.courseid = c.courseid
                    and c1.school = '{Department}'
                    and c1.coursename like '{Subject}%'
                    and (c1.coursename like '%{Content}%'
                    or c1.school like '%{Content}%');
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
    Subject = request.GET.get('Subject')
    Content = request.GET.get('SearchContent')
    if Subject == 'all':
        Subject = ''
    if Department == '':
        Department = 'all'
    with connection.cursor() as cursor:

        if request.method == 'GET':
            if Department == 'all':
                cursor.execute(
                f"""
                SELECT *
                FROM `courses` 
                where courses.courseid not in 
                (SELECT courseid FROM comments)
                and courses.coursename like '{Subject}%'
                and (courses.coursename like '%{Content}%'
                or courses.school like '%{Content}%');
                """
            )
            else:
                cursor.execute(
                    f"""
                  SELECT *
                    FROM `courses` 
                where courses.courseid not in 
                (SELECT courseid FROM comments)
                    and courses.school = '{Department}'
                    and courses.coursename like '{Subject}%'
                    and (courses.coursename like '%{Content}%'
                    or courses.school like '%{Content}%');
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
def knn(request):
    with connection.cursor() as cursor:
        userid = request.GET.get('userid')
        if request.method == 'GET':
            cursor.execute(
                """
                SELECT courses.COURSEID, comments.SCORE
                FROM `comments` , `courses`
                where userid = %s
                and comments.courseid = courses.courseid;
                """%userid
            )
            commentedCourses = cursor.fetchall()
            print(commentedCourses)
            cursor.execute(
                """
                SELECT USERID
                FROM USERS;
                """
            )
            data = cursor.fetchall()
            allUsers = [data[i][0] for i in range(len(data))]
            print(allUsers)
            distance = -1
            recommendID = -1
            recommendUsers = []
            for user in allUsers:
                d = 0
                if str(user) != userid:
                    print(user)
                    cursor.execute(
                        """
                        SELECT courseid,score
                        FROM comments
                        where userid = %s
                        """%user
                    )
                    for course in commentedCourses:
                        cid = course[0]
                        score = course[1]
                        cursor.execute(
                        f"""
                        SELECT score
                        FROM comments
                        where userid = {user}
                        and courseid = {cid};
                        """
                        )
                        othersScore = cursor.fetchall()
                        if othersScore  == []:
                            d += 3 #how to determine this distance
                        else:
                            d += abs(othersScore[0][0] - score)
                    recommendUsers.append((user,d))
            recommendUsers = sorted(recommendUsers,key=lambda x:x[1])
            print(recommendUsers)
            for recommendUser in recommendUsers:
                recommendID = recommendUser[0]
                print(recommendID)
                cursor.execute(
                    f"""
                    SELECT courses.COURSEID, courses.COURSENAME
                    FROM `comments`, `courses`
                    where comments.courseid = courses.courseid
                    and comments.userid = {recommendID}
                    and courses.courseid not in (
                        SELECT COURSEID
                        FROM comments
                        where comments.userid = {userid}
                    );
                    """
                )
                recommendCourses = cursor.fetchall()
                if recommendCourses != []:
                    break
                if len(recommendCourses) > 5:
                    recommendCourses = recommendCourses[:6]
            # print(recommendCourses)
            columns = ['courseID','courseName']

            data = [dict(zip(columns, row)) for row in recommendCourses]
            # print(data)
            response = JsonResponse(data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response