from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
