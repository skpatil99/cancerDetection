from django import forms
from .models import PatientDetail


class PatientDetailForm(forms.ModelForm):
    class Meta:
        model = PatientDetail
        fields = ['PatientID','FirstName', 'LastName','Age','Gender','BloodImage',]

    def clean_FirstName(self):
        FirstName = self.cleaned_data['FirstName']
        return FirstName[0].upper() + FirstName[1:].lower()

    def clean_LastName(self):
        LastName = self.cleaned_data['LastName']
        return LastName[0].upper() + LastName[1:].lower()

    def clean_Age(self):
        Age = self.cleaned_data['Age']
        return Age

    def clean_Gender(self):
        Gender = self.cleaned_data['Gender']
        return Gender[0].upper() + Gender[1:].lower()
