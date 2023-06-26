from django.contrib import admin
from django.urls import include, path, re_path

from error_handler import views

handler401 = views.Http401ErrorView.as_view()
handler404 = views.Http404ErrorView.as_view()
handler500 = views.Http500ErrorView.as_view()

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("faculty/", include("faculty.urls", namespace="faculty")),
    path("student/", include("student.urls", namespace="student")),
    path("admin/", admin.site.urls),
    path("401/", handler401, name="handler401"),
    path("404/", handler404, name="handler404"),
    path("500/", handler500, name="handler500"),
    re_path(r"^.*/$", handler404, name="handler404"),
]
