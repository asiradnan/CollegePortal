from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

def date_validator(x):
    if x>date.today():
        raise ValidationError("Date can not be in the future.")
    

class Club(models.Model):
    club_name = models.CharField(max_length=100, primary_key=True)
    established=models.DateField(validators=[date_validator])
    supervisor = models.ForeignKey('Academics.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name
    
    def save(self,*args,**kwargs):
        self.club_name=self.club_name.title()
        super().save(self,*args,**kwargs)

class Membership(models.Model):
    POSITION_CHOICES = [
        ('Member', 'Member'),
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
    ]

    student = models.ForeignKey('Academics.Student', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)