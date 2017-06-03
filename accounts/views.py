from django.shortcuts import render_to_response
from accounts.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			
			# Create user record
			user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
			user.set_password(password)
			user.save()

			# Create Profile record & add user to group
			is_customer = form.cleaned_data['is_customer']
			profile = Profile(is_customer=is_customer, user=user)
			profile.save()

			if is_customer:
				pass
			else:
				pass

			# Auto login user
			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})

	return render_to_response('accounts/register.html', variables,)


	def logout_page(request):
		logout(request)
		return HttpResponseRedirect('/')

@login_required
def profile(request):

	return render_to_response('accounts/profile.html')