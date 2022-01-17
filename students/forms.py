from django import forms
from .models import StudentInfo, StudentAcademics


class StudentForm(forms.Form):
    roll_no = forms.CharField()
    name = forms.CharField()
    stud_class = forms.CharField()
    school = forms.CharField()
    mobile = forms.CharField()
    address = forms.CharField()
    maths = forms.CharField()
    physics = forms.CharField()
    chemistry = forms.CharField()
    biology = forms.CharField()
    english = forms.CharField()

    def clean(self):
        data = self.cleaned_data # dictionary
        roll_no = data.get("roll_no")
        qs = StudentInfo.objects.filter(roll_no__icontains=roll_no)
        if qs.exists():
            self.add_error("roll_no", f"\"{roll_no}\" is already in use. Please pick another Roll number.")
        return data



# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = StudentInfo
#         fields = ["roll_no", "name", "stud_class", "school", "mobile", "address"]





