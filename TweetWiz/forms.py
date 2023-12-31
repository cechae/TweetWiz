
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "What's on your mind?",
                "class": "textarea is-success is-normal",
            }
        ),
        label="",)

    class Meta:
        model = Tweet
        exclude = ("user", )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
    
    