from django import forms
from .models import Student, Teacher, Principal, Department, CLASS, ContactNumber

shared_input_classes = 'mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:outline-none focus:ring-1 focus:ring-primary-500 focus:border-primary-500'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'CLASS', 'address', 'is_captain']
        widgets = {
            'name': forms.TextInput(attrs={'class': shared_input_classes}),
            'student_id': forms.TextInput(attrs={'class': shared_input_classes}),
            'CLASS': forms.Select(attrs={'class': shared_input_classes}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': shared_input_classes}),
            'is_captain': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-primary-600 focus:ring-primary-500'})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'dept_name', 'dept_designation', 'joining_date', 'address', 'designation']
        widgets = {
            'name': forms.TextInput(attrs={'class': shared_input_classes}),
            'dept_name': forms.Select(attrs={'class': shared_input_classes}),
            'dept_designation': forms.Select(attrs={'class': shared_input_classes}),
            'joining_date': forms.DateInput(attrs={'type': 'date', 'class': shared_input_classes}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': shared_input_classes}),
            'designation': forms.TextInput(attrs={'class': shared_input_classes}),
        }

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = ['name', 'designation', 'joining_date', 'address', 'room_number', 'building_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': shared_input_classes}),
            'designation': forms.Select(attrs={'class': shared_input_classes}),
            'joining_date': forms.DateInput(attrs={'type': 'date', 'class': shared_input_classes}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': shared_input_classes}),
            'room_number': forms.TextInput(attrs={'class': shared_input_classes}),
            'building_number': forms.TextInput(attrs={'class': shared_input_classes}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'room_number', 'building_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': shared_input_classes}),
            'room_number': forms.TextInput(attrs={'class': shared_input_classes}),
            'building_number': forms.TextInput(attrs={'class': shared_input_classes}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = CLASS
        fields = ['class_code', 'room_number', 'building_number']
        widgets = {
            'class_code': forms.TextInput(attrs={'class': shared_input_classes}),
            'room_number': forms.TextInput(attrs={'class': shared_input_classes}),
            'building_number': forms.TextInput(attrs={'class': shared_input_classes}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactNumber
        fields = ['number']
        widgets = {
            'number': forms.TextInput(attrs={'class': shared_input_classes})
        }
