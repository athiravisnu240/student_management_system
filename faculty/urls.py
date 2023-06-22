from django.urls import path

from faculty import views

app_name = "faculty"

urlpatterns = [
    # path('faclogin/', views.faclogin, name='faclogin'),
    # path('updatedprofile/<str:pk>/', views.updatedprofile, name='updatedprofile'),
    # path('editatt/<str:pk>/<str:course>/<str:class>/', views.editatt, name='editatt'),
    # path('updatedindex/<str:pk>/<str:department>/', views.updatedindex, name='updatedindex'),
    # path('updatedadd/<str:pk>/', views.updatedadd, name='updatedadd'),
    # path('fac_report/<str:pk>/<str:clat>/<str:cout>/', views.fac_report, name='fac_report'),
    path("<int:pk>/dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
