from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('helloworld', views.hello_world, name='helloworld'), 
    path('course', views.course, name='course'),
]