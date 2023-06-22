from django.contrib import admin

from accounts.models import Admin, Advisor, Teacher

admin.site.register(Admin)
admin.site.register(Advisor)
admin.site.register(Teacher)
