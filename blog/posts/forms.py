from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].widget.attrs['readonly'] = True
        
    class Meta(UserCreationForm.Meta):
        model = Post
        fields = (
            'text',
            'author',
            'group',
        )


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'text',
            'group',
        )