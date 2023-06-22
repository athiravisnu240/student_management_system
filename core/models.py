from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

DAYS_CHOICES = [
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
]



class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserModel(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.code


class Department(models.Model):
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.code


class Division(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    max_total_students = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.code


class Course(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name


class Calendar(TimeStampedModel):
    date = models.DateField()
    day = models.CharField(max_length=9, choices=DAYS_CHOICES, blank=False)

    def __str__(self):
        return f"{self.date} ({self.day})"


class Slot(TimeStampedModel):
    period_number = models.PositiveSmallIntegerField(
        primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Period - {self.period_number} ({self.start_time}-{self.end_time})"


class Holiday(TimeStampedModel):
    date = models.DateField(primary_key=True)
    description = models.CharField(max_length=100)


class Timetable(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=DAYS_CHOICES, blank=False)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("division", "course", "day")

