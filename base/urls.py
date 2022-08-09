from django.urls import path
from . import views

app_name='base'

urlpatterns = [
    path('', views.homeView, name='Home'),
    path('register/', views.registerView, name='Resgister'),
    path('login/', views.loginView, name='Login' ),
    path('logout/', views.logoutView, name='LogOut'),

    path('jobs/', views.allJobsView, name='Jobs'),
]
