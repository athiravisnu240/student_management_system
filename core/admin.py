from django.contrib import admin

from core.models import Calendar, Course, Department, Division, Holiday, Slot, Timetable

admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Course)
admin.site.register(Calendar)
admin.site.register(Slot)
admin.site.register(Holiday)
admin.site.register(Timetable)
