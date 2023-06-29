from django.db import models

from core.models import BaseUserModel, Course, Division
from faculty.models import Faculty


class Admin(BaseUserModel):
    pass


class Advisor(BaseUserModel):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty} ({self.division})"
