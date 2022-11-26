from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from app.models import Blog,Comment
class Signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['user','title','discription']

class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['blogger','comment']
