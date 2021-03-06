from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.template.loader import render_to_string

from .models import Register, Profile
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django import forms

from .forms import SignUpForm, SignUpForm_crispy
from .tokens import account_activation_token

# Create your views here.


@login_required
def special(request) :
	print "you are special"
	return HttpResponse("youare special")

@login_required
def success_login(request) : 
	print "youre login"
	context = {
		'loginvalue' : 1, 
	}
	return render(request, 'registration/success_login.html', context)

@login_required
def user_logout(request) :
	logout(request)
	#homepagereturn HttpResponseRedirect(reverse('index_register'))
	return redirect('homepage')
	
def index_register(request) :
	if request.method == 'POST' :
		#form = SignUpForm(data=request.POST)
		form = SignUpForm_crispy(data=request.POST)
		print "creating form %s"%(form.is_valid())
		print request.POST
		if form.is_valid() :
			print "enter if"
			
			user = form.save() #save to table user_auth, 		
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.gender = form.cleaned_data.get('gender')
			user.is_active = False
			
			user.save()			#will trigger signal decorator in models.py (post_save)
			current_site = get_current_site(request)
			subject = 'Please activate your account'
			message = render_to_string('registration/activation_request.html', {
				'user' : user,
				'domain' : current_site.domain,
				'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
				'token' : account_activation_token.make_token(user),
			})
			#user.email_user(subject, message) #testing only not sent via smtp
			email = EmailMessage(
				subject, message, to=[user.profile.email]
			)
			email.send()
			#print email
			#username = form.cleaned_data.get('username')
			#password = form.cleaned_data.get('password1')
			#user = authenticate(username=username, password=password)
			#login(request, user)
			
			print "~~~~~seharusnya sukse"
			return redirect('activation_sent')
	else :
		#form = SignUpForm()
		form = SignUpForm_crispy()
	
	return render(request, 'registration/index_register.html', {'form': form})


def user_login(request) :
	if request.method == 'POST' :
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user :
			if user.is_active :
				print "this user is active"
				login(request, user)
				return HttpResponseRedirect(reverse('success_login'))
			else : #tbh no need to do else
				return HttpResponse("your account still need to be activate")
		else :
			print "no user or someone try to login"
			print "They used username: %s and password: %s"%(username,password)
			#return HttpResponse('invalid username or passwpord')
			return redirect('login_invalid')
	else :
		return render(request, 'registration/login.html')


def show_data(request) :
	print "show data function" 
	pass

def listuser(request) :
	item = Profile.objects.all()

	context = {
		'item' 	:	item,
	}
	return render(request, 'listuser.html', context)

def login_invalid_view(request) :
	return render(request, 'registration/login_invalid.html')

def activation_sent_view(request) :
	return render(request, 'registration/activation_sent.html')


def activation_success_view(request) :
	return render(request, 'registration/activation_success.html')


def activate(request, uidb64, token) :
	try :
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token) :
		user.is_active = True
		user.profile.signup_confirmation = True
		user.save()
		login(request, user)
		return redirect('activation-success')
	else :
		return render(request, 'registration/activation_invalid.html')