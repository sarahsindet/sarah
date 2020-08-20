from django import forms
from .models import Profile,Post,Rating
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','date']
        widgets={
            'technologies':forms.CheckboxSelectMultiple(),
        }


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content','creativity']
        exclude=['overall_score','profile','post']