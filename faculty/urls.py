from django.urls import path,include
from . import views


urlpatterns = [
    path("login/", views.faclogin, name='faclogin'),
    path("<str:pk>/", views.updatedindex, name='updatedindex'),
    path("profile/<str:pk>/", views.updatedprofile, name='updatedprofile'),
    path("add/<str:pk>/", views.updatedadd, name='updatedadd'),
    path("edit_attendance/<str:pk>/", views.editatt, name='editatt'),
    path("report/<str:pk>/", views.fac_report, name='fac_report'),
]
