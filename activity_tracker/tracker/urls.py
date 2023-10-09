from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('LoginStudent', views.LoginStudent, name='LoginStudent'),
    path('LoginMentor', views.LoginMentor, name='LoginMentor'),
    path('HomeMentor', views.HomeMentor, name='HomeMentor'),
    path('saishruthi', views.saishruthi, name='saishruthi'),
    path('activitypoints', views.activitypoints, name='activitypoints'),
    path('notifications', views.notifications, name='notifications'),
]