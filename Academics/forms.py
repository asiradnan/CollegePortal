from django import forms
from .models import CLASS,Student,Teacher,Department,ContactNumber,Principal


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','student_id','CLASS','address']
        labels = {
            'student_id': 'Student ID',
            'CLASS':'Class',
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','designation','dept_name','joining_date','address','dept_designation']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'dept_designation': 'Department designation',
            'dept_name':'Department Name',
        }

class PrincipalForm(forms.ModelForm):
    class Meta:
        model=Principal
        fields=['name','designation','joining_date','address','room_number','building_number']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields=['name','room_number','building_number']
    
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactNumber
        fields=['number']
        labels = {
            'number' : 'Add a Contact Number'
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model=CLASS
        fields=['class_code','room_number','building_number']
