from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('helloworld/', views.hello_world, name='helloworld'), 
    path('get_users/', views.get_users, name="get_users"), 
    path('register_user/', views.register_user, name="register_user")
]