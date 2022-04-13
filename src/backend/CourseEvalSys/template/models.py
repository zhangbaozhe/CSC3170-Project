from django.db import models

class Users(models.Model):
    User_ID = models.IntegerField('User_ID',db_column='User_ID',primary_key=True)
    User_name = models.CharField('User_name',db_column='User_name',max_length=255,null=False)
    Password = models.CharField('Password',db_column='Password',max_length=255,null=False)
    class Meta:
        db_table = 'Users'

class Courses(models.Model):
    Course_ID = models.IntegerField('Course_ID',db_column='Course_ID',primary_key=True)
    Course_Name = models.CharField('Course_name',db_column='Course_Name',max_length=255,null=False)
    Department = models.CharField('Department',db_column='Department',max_length=255,null=False)
    Is_Valid = models.BooleanField('Is_Valid',db_column='Is_Valid',null=False) #0:not valid, 1:valid
    Final_Score = models.FloatField('FinalScore',db_column='Final_Score',null=True) #average score?
    class Meta:
        db_table = 'Courses'

class Comments(models.Model):
    Comment_ID = models.IntegerField('Comment_ID',db_column='Comment_ID',primary_key=True,null=False)
    User_ID = models.ForeignKey('Users',to_field='User_ID',related_name='ID_of_User',on_delete=models.CASCADE)
    Course_ID = models.ForeignKey('Courses',to_field='Course_ID',related_name='CourseID',on_delete=models.CASCADE)
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
    User_ID = models.ForeignKey('Users',to_field='User_ID',related_name='UserID',on_delete=models.CASCADE)
    CommentID = models.OneToOneField(Comments, related_name='ID_of_Comment',primary_key=True,on_delete=models.CASCADE) # 0:dislike, 1:like
    Status = models.BooleanField('Status',db_column='Status',null=False)
    class Meta:
        db_table = 'CommentsLikeStatus'