from django import forms
from .models import Club,Membership

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields= ['club_name','supervisor','established']
        widgets = {
            'established': forms.DateInput(attrs={'type': 'date'}),
        }

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields= ['club','position']