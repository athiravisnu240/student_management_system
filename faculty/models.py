from django.db import models

from core.models import BaseUserModel, Course, Department, Division


class Faculty(BaseUserModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    divisions = models.ManyToManyField(Division)
    courses = models.ManyToManyField(Course)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.code})"
