from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseUserModel, Course, Department, Division, TimeStampedModel

LEAVE_CHOICES = [
    ("ml", "Medical Leave"),
    ("od", "On Duty"),
]


class Student(BaseUserModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    in_out = models.CharField(max_length=5)
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, blank=True, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.code})"


class Attendance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.BooleanField(default=False)
    periods = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )

    def __str__(self):
        return f"{self.student} ({self.date})"


class Leave(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    leave_type = models.CharField(
        max_length=9,
        choices=LEAVE_CHOICES,
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        approved = "Approved" if self.approved else "Not Approved"
        return f"{self.leave_type}({approved})"
