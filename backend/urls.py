from django.urls import path
from backend import views, sec_comment

app_name = 'backend'

urlpatterns = [
    path('course', views.course, name='course'), # TODO: add '/'
    path('helloworld/', views.hello_world, name='helloworld'), 
    path('login/', views.login),
    path('get_users/', views.get_users, name="get_users"), 
    path('register_user/', views.register_user, name="register_user")
    path('seccomment/', sec_comment.sec_comment),
]