from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    post_serial=models.AutoField(primary_key=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=10000)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    date=models.DateField(auto_now_add=True, editable=False)
