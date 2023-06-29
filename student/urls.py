from django.urls import path, include
from student import views

app_name = "student"

urlpatterns = [
    # path("login/", views.studlogin, name="studlogin"),
    # path("<str:pk>/", views.studindex, name="studindex"),
    # path("profile/<str:pk>/", views.studprofile, name="studprofile"),
    # path("add/<str:pk>/", views.studadd, name="studadd"),
    # path("report/<str:pk>/", views.stud_report, name="stud_report"),
    path("<int:pk>/dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("attendance/add/", views.AddAttendanceView.as_view(), name="add_attendance"),
    path("attendance/<int:pk>/update", views.UpdateAttendanceView.as_view(), name="update_attendance"),
    path("attendance/<int:pk>/delete", views.DeleteAttendanceView.as_view(), name="delete_attendance"),
]
