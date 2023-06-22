from typing import Any, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


class HomeView(views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        url = super().get_redirect_url(*args, **kwargs)
        if user.is_authenticated:
            if hasattr(user, "student") and user.student is not None:
                url = reverse_lazy("student:dashboard", kwargs={"pk": user.student.id})
            elif hasattr(user, "faculty") and user.faculty is not None:
                url = reverse_lazy("faculty:dashboard", kwargs={"pk": user.faculty.id})
            else:
                url = "/404"
        else:
            url = reverse_lazy("accounts:login")

        return url


class DashboardView(LoginRequiredMixin, views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        url = super().get_redirect_url(*args, **kwargs)

        if hasattr(user, "student") and user.student is not None:
            url = reverse_lazy("student:dashboard", kwargs={"pk": user.student.id})
        elif hasattr(user, "faculty") and user.faculty is not None:
            url = reverse_lazy("faculty:dashboard", kwargs={"pk": user.faculty.id})
        else:
            url = "/404"

        return url
