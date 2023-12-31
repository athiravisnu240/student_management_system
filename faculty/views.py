# import csv
# from django.contrib import messages
# from django.http import HttpResponse
from typing import Any, Dict
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Holiday

from faculty.models import Faculty
from student.forms import AttendanceForm
from student.models import Attendance, Student


class DashboardView(LoginRequiredMixin, views.DetailView):
    template_name = "faculty/dashboard.html"
    model = Faculty
    context_object_name = "faculty"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        students = Student.objects.filter(department__faculty=self.get_object())
        holidays = Holiday.objects.values("date", "description")
        holiday_data = [
            {"title": h["description"], "start": h["date"].strftime("%Y-%m-%d")}
            for h in holidays
        ]
        attendances = Attendance.objects.filter(student__in=students)
        context.update(
            {
                "students": students,
                "holidays": holiday_data,
                "attendances": attendances,
                "attendance_form": AttendanceForm,
            }
        )
        return context
