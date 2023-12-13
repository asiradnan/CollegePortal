from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title','content','pdf_file']
        labels={
            'title' : 'Notice Title',
            'content': "Notice",
            'pdf_file' : 'PDF File (optional)'
        }