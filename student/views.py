# import csv
# from django.forms import modelform_factory
# from django.http import HttpRequest, HttpResponse
# from django.template import loader
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from student.forms import AttendanceForm

from student.models import Attendance, Student


class DashboardView(LoginRequiredMixin, views.DetailView):
    template_name = "student/dashboard.html"
    model = Student
    context_object_name = "student"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        attendance = getattr(self.get_object(), "attendance_set", None)

        context.update({})
        return context


class AddAttendanceView(views.View):
    model = Attendance
    form_class = AttendanceForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        url = request.META.get("HTTP_REFERER")
        if form.is_valid():
            attendance = form.save()
            messages.success(request, _("Attendance added successfully!"))
        else:
            messages.success(request, _("Can't add Attendance!"))

        return redirect(url)


class UpdateAttendanceView(LoginRequiredMixin, views.View):
    model = Attendance
    form_class = AttendanceForm

    def get(self, request, *args, **kwargs):
        attendance = Attendance.objects.get(pk=kwargs.get("pk"))
        html = self.form_class(instance=attendance).as_table()
        return HttpResponse(html)
    
    def post(self, request, *args, **kwargs):
        attendance = Attendance.objects.get(pk=kwargs.get("pk"))
        form = self.form_class(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
        return redirect(request.META.get("HTTP_REFERER"))
    
class DeleteAttendanceView(LoginRequiredMixin,views.View):
    model = Attendance
    def get(self, request, *args, **kwargs) -> str:
        attendance = Attendance.objects.get(pk=kwargs.get("pk"))
        attendance.delete()
        return redirect(request.META.get("HTTP_REFERER"))


# from login.models import (
#     Department,
#     Admin,
#     Division,
#     Student,
#     Faculty,
#     Calender,
#     Course,
#     Attendance,
#     Timetable,
#     Teacher,
# )
# from django.contrib import messages

# # Create your views here.
# stu = ""
# dep = ""
# cla = ""
# cou = ""


# def initial(stut, dept):
#     global stu, dep
#     stu = stut
#     dep = dept
#     return


# def tial(clat, cout):
#     global cla, cou
#     cla = clat
#     cou = cout
#     print(clat)
#     print(cout)
#     return


# def studlogin(request):
#     if request.method == "POST":
#         u, p = request.POST.get("email"), request.POST.get("password")
#         print(u, p)
#         stud = Student.objects.filter(stud_id=u)
#         if stud.exists():
#             if stud.get().s_password == p:
#                 d = stud.get().department.code
#                 initial(u, d)
#                 return redirect(reverse_lazy("studprofile", kwargs={"pk": u}))
#             else:
#                 messages.error(request, "Invalid Credentials")
#                 return redirect("index")
#         else:
#             messages.error(request, "No such User exists")
#             return redirect("index")
#     else:
#         messages.error(request, "Enter Credentials")
#         return redirect("index")


# def studprofile(request: HttpRequest, *args, **kwargs):
#     stu = kwargs.get("pk")
#     if request.method == "POST":
#         try:
#             stud = Student.objects.filter(stud_id=stu).first()
#             form = modelform_factory(Student, fields="__all__")
#             form.instance = stud
#             if form.is_valid():
#                 stud = form.save()
#             else:
#                 messages.error(request, "Oops something went wrong!")
#                 redirect(reverse_lazy("studprofile", kwargs={"pk": stu}))

#         except Exception as ex:
#             messages.error(request, f"Oops something went wrong! {ex}")
#             return redirect(reverse_lazy("studprofile", kwargs={"pk": stu}))
#     stud = Student.objects.filter(stud_id=stu).first()
#     return render(request, "studprofile.html", {"stu": stud})


# def studindex(request, *args, **kwargs):
#     stu = kwargs.get("pk")
#     dept = Department.objects.filter(dept_id=dep).first()
#     stud = Student.objects.filter(stud_id=stu).first()
#     atte = Attendance.objects.all().filter(stud_id=stu).order_by("-date")
#     cour, cou = [], []
#     for i in atte:
#         if i.course not in cour:
#             cour.append(i.course)
#     for i in cour:
#         cou.append(
#             [
#                 i.course_id,
#                 0,
#                 Attendance.objects.all()
#                 .filter(stud_id=stu, course_id=i.course_id)
#                 .count(),
#                 0,
#                 i.course_name,
#             ]
#         )
#     for i in atte:
#         for j in range(len(cou)):
#             if i.course.code == cou[j][0]:
#                 if i.presence:
#                     cou[j][1] += 1
#     for i in cou:
#         i[3] = int(i[1] / i[2] * 100)
#     coud = []
#     for i in cou:
#         if i[3] <= 75:
#             coud.append(i)
#     print(stud)
#     return render(request, "studindex.html", context={"stud": stud, "cou": coud})


# def studadd(request: HttpRequest, *args, **kwargs):
#     stu = kwargs.get("pk")
#     dept = Department.objects.filter(dept_id=dep).first()
#     stud = Student.objects.filter(stud_id=stu).first()
#     atte = Attendance.objects.all().filter(stud_id=stu).order_by("-date")
#     cour, cou = [], []
#     for i in atte:
#         if i.course not in cour:
#             cour.append(i.course)
#     for i in cour:
#         cou.append(
#             [
#                 i.course_id,
#                 0,
#                 Attendance.objects.all()
#                 .filter(stud_id=stu, course_id=i.course_id)
#                 .count(),
#                 0,
#                 i.course_name,
#             ]
#         )
#     for i in atte:
#         for j in range(len(cou)):
#             if i.course.code == cou[j][0]:
#                 if i.presence:
#                     cou[j][1] += 1
#     for i in cou:
#         i[3] = int(i[1] / i[2] * 100)
#     print(cou)
#     return render(request, "studadd.html", {"stud": stud, "cou": cou})


# def stud_report(request, *args, **kwargs):
#     stu = kwargs.get("pk")
#     if request.method == "POST":
#         data = request.POST
#         p = next(key for key in data if key != "csrfmiddlewaretoken")
#         tial(cla, p)

#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = 'attachment; filename="AttendanceReport.csv"'

#     stud = Student.objects.filter(stud_id=stu).first()
#     atte = Attendance.objects.filter(course_id=cou, stud_id=stu).order_by(
#         "fac_id", "date"
#     )

#     writer = csv.writer(response)
#     writer.writerow(["Fac-Id", "Class-Id", "Dept", "Course-Id", "Date", "Status"])

#     for i in atte:
#         status = "Present" if i.presence else "Absent"
#         writer.writerow(
#             [
#                 i.faculty.fac_id,
#                 stud.division.code,
#                 stud.department.code,
#                 cou,
#                 i.date,
#                 status,
#             ]
#         )

#     return response
