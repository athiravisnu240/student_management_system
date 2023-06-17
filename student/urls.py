from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.studindex, name='studindex'),
    path('login/', views.studlogin, name='studlogin'),
    path('profile/<str:pk>/', views.studprofile, name='studprofile'),
    path('add/', views.studadd, name='studadd'),
    path('report/<str:pk>/', views.stud_report, name='stud_report'),
]
