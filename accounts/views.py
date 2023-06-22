from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from faculty.models import Faculty

from student.models import Student


class LoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials")
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        model = self.request.POST.get("model")
        success_url = reverse_lazy("core:home")
        if model == "Student":
            student = Student.objects.filter(user=self.request.user)
            if student.exists():
                success_url = reverse_lazy("student:dashboard", kwargs={"pk": student.first().pk})
        elif model == "Faculty":
            faculty = Faculty.objects.filter(user=self.request.user)
            if faculty.exists():
                success_url = reverse_lazy("faculty:dashboard", kwargs={"pk": faculty.first().pk})
        else:
            success_url = "/404/"
        return success_url


class LogoutView(LogoutView):
    template_name = "accounts/logged_out.html"
