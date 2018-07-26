from django import forms
from .models import Entry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#these are for validating errors
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _




class Reserve(forms.ModelForm):	
	class Meta:
		model = Entry
		fields = ('name', 'number', 'comment', 'dedication',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )