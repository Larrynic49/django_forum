from django import forms

from dataclasses import fields
from .models import Post
from pyexpat import model


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'