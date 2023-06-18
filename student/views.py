import csv
from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from login.models import (
    Department,
    Admin,
    Class,
    Student,
    Faculty,
    Calender,
    Course,
    Attendance,
    Timetable,
    Teache,
)
from django.contrib import messages

# Create your views here.
stu = ""
dep = ""
cla = ""
cou = ""


def initial(stut, dept):
    global stu, dep
    stu = stut
    dep = dept
    return


def tial(clat, cout):
    global cla, cou
    cla = clat
    cou = cout
    print(clat)
    print(cout)
    return


def studlogin(request):
    if request.method == "POST":
        u, p = request.POST.get("email"), request.POST.get("password")
        stud = Student.objects.filter(stud_id=u)
        if stud.exists():
            if stud.get().s_password == p:
                d = stud.get().dept_id.dept_id
                initial(u, d)
                return redirect(reverse_lazy("studprofile", kwargs={"pk": u}))
            else:
                messages.error(request, "Invalid Credentials")
                return redirect("index")
        else:
            messages.error(request, "No such User exists")
            return redirect("index")
    else:
        messages.error(request, "Enter Credentials")
        return redirect("index")


def studprofile(request: HttpRequest, *args, **kwargs):
    stu = kwargs.get("pk")
    if request.method == "POST":
        try:
            stud = Student.objects.filter(stud_id=stu)
            form = modelform_factory(Student, fields="__all__")
            form.instance = stud
            if form.is_valid():
                stud = form.save()
            else:
                messages.error(request, "Oops something went wrong!")
                redirect(reverse_lazy("studprofile", kwargs={"pk": stu}))

        except Exception as ex:
            messages.error(request, f"Oops something went wrong! {ex}")
            return redirect(reverse_lazy("studprofile", kwargs=kwargs))
    stud = Student.objects.filter(stud_id=stu).first()
    return render(request, "studprofile.html", {"stu": stud})


def studindex(request, *args, **kwargs):
    stu = kwargs.get("pk")
    dept = Department.objects.filter(dept_id=dep)
    stud = Student.objects.filter(stud_id=stu).first()
    atte = Attendance.objects.all().filter(stud_id=stu).order_by("-date")
    cour, cou = [], []
    for i in atte:
        if i.course_id not in cour:
            cour.append(i.course_id)
    for i in cour:
        cou.append(
            [
                i.course_id,
                0,
                Attendance.objects.all()
                .filter(stud_id=stu, course_id=i.course_id)
                .count(),
                0,
                i.course_name,
            ]
        )
    for i in atte:
        for j in range(len(cou)):
            if i.course_id.course_id == cou[j][0]:
                if i.presence:
                    cou[j][1] += 1
    for i in cou:
        i[3] = int(i[1] / i[2] * 100)
    coud = []
    for i in cou:
        if i[3] <= 75:
            coud.append(i)
    return render(request, "studindex.html", {"stud": stud, "cou": coud})


def studadd(request: HttpRequest, *args, **kwargs):
    stu = kwargs.get("pk")
    dept = Department.objects.filter(dept_id=dep).first()
    stud = Student.objects.filter(stud_id=stu).first()
    atte = Attendance.objects.all().filter(stud_id=stu).order_by("-date")
    cour, cou = [], []
    for i in atte:
        if i.course_id not in cour:
            cour.append(i.course_id)
    for i in cour:
        cou.append(
            [
                i.course_id,
                0,
                Attendance.objects.all()
                .filter(stud_id=stu, course_id=i.course_id)
                .count(),
                0,
                i.course_name,
            ]
        )
    for i in atte:
        for j in range(len(cou)):
            if i.course_id.course_id == cou[j][0]:
                if i.presence:
                    cou[j][1] += 1
    for i in cou:
        i[3] = int(i[1] / i[2] * 100)
    print(cou)
    return render(request, "studadd.html", {"stud": stud, "cou": cou})


def stud_report(request, *args, **kwargs):
    stu = kwargs.get("pk")
    if request.method == "POST":
        data = request.POST
        p = next(key for key in data if key != "csrfmiddlewaretoken")
        tial(cla, p)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="AttendanceReport.csv"'

    stud = Student.objects.filter(stud_id=stu).first()
    atte = Attendance.objects.filter(course_id=cou, stud_id=stu).order_by("fac_id", "date")

    writer = csv.writer(response)
    writer.writerow(["Fac-Id", "Class-Id", "Dept", "Course-Id", "Date", "Status"])

    for i in atte:
        status = "Present" if i.presence else "Absent"
        writer.writerow([
            i.fac_id.fac_id,
            stud.class_id.class_id,
            stud.dept_id.dept_id,
            cou,
            i.date,
            status,
        ])

    return response
