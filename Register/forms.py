from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm) :
	first_name = forms.CharField(max_length=30, help_text='First Name')
	last_name = forms.CharField(max_length=30, help_text='Last Name')
	email = forms.EmailField(max_length=200, help_text='Email')

	class Meta :
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		
	##adding class  and placeholder attribute 
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs.update({'placeholder':('Username')})
		self.fields['first_name'].widget.attrs.update({'placeholder':('Your first name')})
		self.fields['last_name'].widget.attrs.update({'placeholder':('Your last name')})
		self.fields['email'].widget.attrs.update({'placeholder':('Email address')})
		self.fields['password1'].widget.attrs.update({'placeholder':('Your password')})
		self.fields['password2'].widget.attrs.update({'placeholder':('Retype password')})
    