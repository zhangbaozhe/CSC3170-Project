from django.urls import path
from backend import views
from backend import SubmitComment

app_name = 'backend'

urlpatterns = [
    path('course', views.course, name='course'), # TODO: add '/'
    path('helloworld/', views.hello_world, name='helloworld'), 
    path('login/', views.login),
    path('get_users/', views.get_users, name="get_users"), 
    path('register_user/', views.register_user, name="register_user"), 
    path('course/submit_comment/', SubmitComment.submit_comment, name="submit_comment"),
]