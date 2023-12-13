from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']
        labels = {
            'content' : 'Write your post',
            'image' : 'You can add image in your post'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['content']
