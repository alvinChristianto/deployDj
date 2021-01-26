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

from .models import Register
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from .forms import SignUpForm
from .tokens import account_activation_token

# Create your views here.


@login_required
def special(request) :
	print "you are special"
	return HttpResponse("youare special")

@login_required
def success_login(request) : 
	print "youre login"
	return render(request, 'registration/success_login.html')

@login_required
def user_logout(request) :
	logout(request)
	return HttpResponseRedirect(reverse('signup_view'))

def index_register(request) :
	if request.method == 'POST' :
		form = SignUpForm(data=request.POST)
		print "creating form %s"%(form.is_valid())
		if form.is_valid() :
			print "enter if"
			user = form.save()		
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
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
			#email.send()
			print email
			#username = form.cleaned_data.get('username')
			#password = form.cleaned_data.get('password1')
			#user = authenticate(username=username, password=password)
			#login(request, user)
			print "~~~~~seharusnya sukse"
			return redirect('activation_sent')
	else :
		form = SignUpForm()
	return render(request, 'registration/index_register.html', {'form': form})




def listuser(request) :
	item = Register.objects.all()
	context = {
		'item' 	:	item,
	}
	return render(request, 'listuser.html', context)


def activation_sent_view(request) :
	return render(request, 'registration/activation_sent.html')


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
		return redirect('/')
	else :
		return render(request, 'registration/activation_invalid.html')