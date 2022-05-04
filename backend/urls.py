from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('course', views.course, name='course'), # TODO: add '/'
    path('helloworld/', views.hello_world, name='helloworld'), 
    path('login/', views.login),
    path('get_users/', views.get_users, name="get_users"), 
    path('register_user/', views.register_user, name="register_user"),
    path('search/', views.search),
    path('search0/', views.search_0),
    path('search1/', views.search_1),
    path('search2/', views.search_2),
]