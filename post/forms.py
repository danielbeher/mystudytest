from django import forms
from post.models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image'
        ]





