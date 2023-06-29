from django import forms

from student.models import Attendance


class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )

    class Meta:
        model = Attendance
        fields = "__all__"
        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "periods": forms.NumberInput(attrs={"class": "form-control"}),
        }
