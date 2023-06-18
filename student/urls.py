from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.studlogin, name="studlogin"),
    path("<str:pk>/", views.studindex, name="studindex"),
    path("profile/<str:pk>/", views.studprofile, name="studprofile"),
    path("add/<str:pk>/", views.studadd, name="studadd"),
    path("report/<str:pk>/", views.stud_report, name="stud_report"),
]
