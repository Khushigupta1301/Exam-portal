from django import forms

from .models import ExamForm


class ExamFormSubmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            base_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (base_class + " portal-input").strip()

    class Meta:
        model = ExamForm
        fields = ["full_name", "course", "year", "address", "phone_number"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full Name"}),
            "course": forms.TextInput(attrs={"placeholder": "Course"}),
            "year": forms.NumberInput(attrs={"placeholder": "Year"}),
            "address": forms.Textarea(attrs={"rows": 3, "placeholder": "Address"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone Number"}),
        }

    def clean_year(self):
        year = self.cleaned_data["year"]
        if year < 1 or year > 8:
            raise forms.ValidationError("Year must be between 1 and 8.")
        return year

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"].strip()
        allowed = set("0123456789+ -")
        if any(char not in allowed for char in phone_number):
            raise forms.ValidationError("Phone number contains invalid characters.")

        digit_count = sum(char.isdigit() for char in phone_number)
        if digit_count < 7 or digit_count > 15:
            raise forms.ValidationError("Phone number must contain 7 to 15 digits.")
        return phone_number