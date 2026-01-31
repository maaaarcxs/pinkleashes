from django import forms
from . models import Review, Appointment


class ReviewMForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "master",
            "rating",
            "comment",
        ]
        widgets = {
            "master": forms.Select(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class AppointmentMForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "customer_name",
            "phone_number",
            "service",
            "master",
            "date",
            "time",
            "comment",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput (attrs={"class": "form-control"}),
            "service": forms.CheckboxSelectMultiple(),
            "master": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }