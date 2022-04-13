from django.db import models

class Users(models.Model):
    User_ID = models.IntegerField('User_ID',db_column='User_ID',primary_key=True)
    User_name = models.CharField('User_name',db_column='User_name',max_length=255,null=False,unique=True)
    Password = models.CharField('Password',db_column='Password',max_length=255,null=False)
    class Meta:
        db_table = 'Users'

class Courses(models.Model):
    Course_ID = models.IntegerField('Course_ID',db_column='Course_ID',primary_key=True)
    Course_Name = models.CharField('Course_name',db_column='Course_Name',max_length=255,null=False,unique=True)
    Department = models.CharField('Department',db_column='Department',max_length=255,null=False)
    Is_Valid = models.BooleanField('Is_Valid',db_column='Is_Valid',null=False) #0:not valid, 1:valid
    Final_Score = models.FloatField('Final_Score',db_column='Final_Score',null=True) #average score?
    Credit = models.IntegerField('Credit',db_column='Credit',null=False,default=3)
    class Meta:
        db_table = 'Courses'

class Comments(models.Model):
    Comment_ID = models.IntegerField('Comment_ID',db_column='Comment_ID',primary_key=True,null=False)
    User_ID = models.ForeignKey(Users,to_field='User_ID',related_name='ID_of_User',on_delete=models.CASCADE)
    Course_ID = models.ForeignKey(Courses,to_field='Course_ID',related_name='CourseID',on_delete=models.CASCADE)
    Semester = models.CharField('Semeste',db_column='Semester',max_length=255,null = False)
    Year = models.IntegerField('Year',db_column='Year',null=False)
    Instructor = models.CharField('Instructor',db_column='Instructor',max_length=255,null=False)
    Score = models.IntegerField('Score',db_column='Score',null=False)
    Content = models.CharField('Content',db_column='Content',max_length=255,null=False)
    Like_Num = models.IntegerField('Like_Num',db_column='Like_Num',null=False)
    Dislike_Num = models.IntegerField('Dislike_Num',db_column='Dislike_Num',null=False)
    class Meta:
        db_table = 'Comments'

class CommentsLikeStatus(models.Model):
    # Status_ID = models.AutoField(primary_key=True,default=1)
    Status_ID = models.IntegerField('Status_ID',db_column='Status_ID',primary_key=True,null=False,default=1)
    User_ID = models.ForeignKey(Users,to_field='User_ID',related_name='UserID',on_delete=models.CASCADE)
    CommentID = models.ForeignKey(Comments, related_name='ID_of_Comment',on_delete=models.CASCADE) # 0:dislike, 1:like
    Status = models.BooleanField('Status',db_column='Status',null=False)
    class Meta:
        db_table = 'CommentsLikeStatus'
        constraints = [
            models.UniqueConstraint(fields=['User_ID', 'CommentID'], name='like_id'),
        ]

class MultiComment(models.Model):
    Multi_Comment_ID = models.IntegerField('Multi_Comment_ID',db_column='Multi_Comment_ID',primary_key=True,null=False)
    User_ID = models.ForeignKey(Users,to_field='User_ID',related_name='UID',on_delete=models.CASCADE)
    Content = models.CharField('Content',db_column='Content',max_length=255,null=False)
    Lower_Comment_ID = models.IntegerField('Lower_Comment_ID',db_column='Lower_Comment_ID',null=True)
    class Meta:
        db_table = 'MultiComment'

        