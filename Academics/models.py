from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

def room_validate(x):
    if not x.isdigit():
        raise ValidationError('Enter a valid Room Number')
    
def building_validate(x):
    if not x.isdigit():
        raise ValidationError('Enter a valid Building Number')
    
def id_validate(x):
    if len(x) != 6 or not x.isdigit():
        raise ValidationError('Enter your valid Student ID.')
    
def name_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Name should not contain digits.')

def desig_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Designation should not contain digits.')
    
def date_validator(value):
    if value > date.today():
        raise ValidationError('Date cannot be in the future.')
    
def contact_validator(x):
    if not x.isdigit() or len(x)<11:
        raise ValidationError("Enter a valid Contact Number")
   

class CLASS(models.Model):
    class_code=models.CharField(max_length=100,primary_key=True)
    room_number=models.CharField(max_length=4,validators=[room_validate])
    building_number=models.CharField(max_length=4,validators=[building_validate])

    def __str__(self):
        return f"{self.class_code}"
    

class Student(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,validators=[name_validator])
    student_id=models.CharField(max_length=10,validators=[id_validate])
    CLASS=models.ForeignKey(CLASS,on_delete=models.SET_NULL,null=True)
    address=models.TextField(max_length=500)
    is_captain=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def make_captain(self):
        self.is_captain = True
        self.save()
    def save(self,*args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class Department(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    room_number=models.CharField(max_length=4,validators=[room_validate])
    building_number=models.CharField(max_length=4,validators=[building_validate])

    def __str__(self):
        return f"{self.name}"
    def save(self, force_insert=False, force_update=False):
        self.name = self.name.upper()
        super(Department, self).save(force_insert, force_update)


class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,validators=[name_validator])
    dept_name=models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    POSITION_CHOICES=[('Chairman','Chairman'),('Vice Chairman','Vice Chairman'),('Member','Member')]
    dept_designation=models.CharField(max_length=100, choices=POSITION_CHOICES)
    joining_date=models.DateField(validators=[date_validator])
    address=models.TextField(max_length=500)
    designation=models.CharField(max_length=100,validators=[desig_validator])

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class ContactNumber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    number=models.CharField(max_length=15,validators=[contact_validator])

    def __str__(self):
        return self.number


class Principal(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=255,validators=[name_validator])
    POSITION_CHOICES=[('Principal','Principal'),('Vice Principal','Vice Principal')]
    designation=models.CharField(max_length=100, choices=POSITION_CHOICES)
    joining_date=models.DateField(validators=[date_validator])
    address=models.TextField(max_length=500)
    room_number=models.CharField(max_length=4,validators=[room_validate],default=5)
    building_number=models.CharField(max_length=4,validators=[building_validate],default=2)

    def save(self,*args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)
    