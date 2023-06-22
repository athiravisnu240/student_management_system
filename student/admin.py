from django.contrib import admin

from student.models import Attendance, Leave, Student

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Leave)
