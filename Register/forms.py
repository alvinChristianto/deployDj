from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SignUpForm(UserCreationForm) :
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
    
	first_name = forms.CharField(max_length=30, help_text='First Name')
	last_name = forms.CharField(max_length=30, help_text='Last Name')
	email = forms.EmailField(max_length=200, help_text='Email')
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

	class Meta :
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'password1', 'password2',) #ordering here
		
	##adding class  and placeholder attribute 
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs.update({'placeholder':('Username')})
		#self.fields['gender'].widget.attrs.update({'class':('form-check form-check-inline')})
		#self.fields['gender'].widget.attrs['class']= 'form-check form-check-inline'
		self.fields['first_name'].widget.attrs.update({'placeholder':('Your first name')})
		self.fields['last_name'].widget.attrs.update({'placeholder':('Your last name')})
		self.fields['email'].widget.attrs.update({'placeholder':('Email address')})
		self.fields['password1'].widget.attrs.update({'placeholder':('Your password')})
		self.fields['password2'].widget.attrs.update({'placeholder':('Retype password')})
  


class SignUpForm_crispy(UserCreationForm):

	def file_size(value):
		checkEmailifExist = value
		duplicate_user = User.objects.filter(email = checkEmailifExist)
		if duplicate_user.exists() :
			raise ValidationError("email already registered, use another email")

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	STATES = (
	    ('', 'Choose...'),
	    ('JKT', 'Jakarta'),
	    ('YOG', 'Yogyakarta'),
	    ('BDG', 'Bandung')
	)

	first_name = forms.CharField(
		label='First Name',
		max_length=200,
		widget=forms.TextInput(attrs={'placeholder': 'First Name' })
	)
	last_name = forms.CharField(
		label='Last Name',
		max_length=200,
		widget=forms.TextInput(attrs={'placeholder': 'Last Name' })
	)
	username = forms.CharField(
		label='Username',
		max_length=20,
		widget=forms.TextInput(attrs={'placeholder': 'Username' })
	)

	email = forms.EmailField(
		max_length=200, 
		widget=forms.TextInput(attrs={'type': 'email', 
									'placeholder': ('E-mail address')}),
		validators=[file_size],
	)

	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	password1 = forms.CharField(
		label='Password', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Your password' }))
	password2 = forms.CharField(
		label='Retype Password', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Retype password' }))
	
	'''
	address_1 = forms.CharField(
		label='Address',
		widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
	)
	address_2 = forms.CharField(
	widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
	)
	city = forms.CharField()
	state = forms.ChoiceField(choices=STATES)
	zip_code = forms.CharField(label='Zip')
	
	check_me_out = forms.BooleanField(required=False)
	'''
	class Meta :
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'password1', 'password2',) #ordering here
		