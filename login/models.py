from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


DAYS_CHOICE=[('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),('thu','Thursday'),('fri','Friday'),('sat','Saturday'),]
LEAVE_CHOICE=[('ml','Medical Leave'),('od','On Duty')]

class Department(models.Model):
    dept_id = models.CharField(max_length=20,primary_key = True)
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class Admin(models.Model):
    admin_id = models.CharField(max_length=20,primary_key = True)
    password =models.CharField(max_length=30)

    def __str__(self):
        return self.admin_id

class Class(models.Model):
    class_id = models.CharField(max_length=20,primary_key=True)
    total_students = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])
    
    def __str__(self):
        return self.class_id

class Student(models.Model):
    stud_id = models.CharField(max_length=20,primary_key=True)
    s_password = models.CharField(max_length=30)
    in_out = models.CharField(max_length=5)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Faculty(models.Model):
    fac_id = models.CharField(max_length=20,primary_key=True)
    f_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.fac_id

class Calender(models.Model):
    i=models.AutoField(primary_key=True)
    dates = models.DateField()
    day = models.CharField(max_length=9,choices=DAYS_CHOICE,default=None,blank=False)

class Course(models.Model):
    course_id = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=50)
    credits = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])

    def __str__(self):
        return self.course_name

class Attendance(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])
    periods = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(8)])
    
    class Meta:
        unique_together = (("stud_id","course_id","date"),)

    def __str__(self):
        return f"{self.date}"

class Slot(models.Model):
    period_id=models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(8)],primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"

class Holiday(models.Model):
    date = models.DateField(primary_key=True)
    description = models.CharField(max_length=100)

class Advisor(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.fac_id

class Leave(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=9,choices=LEAVE_CHOICE,default=None,blank=False)
    approved = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])

    def __str__(self):
        return f"{self.leave_type}({self.approved})"



class Timetable(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=9,choices=DAYS_CHOICE,default=None,blank=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    periods_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("class_id", "course_id","day"),)

class Teache(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("course_id", "class_id"),)

    def __str__(self) -> str:
        return self.fac_id

    
