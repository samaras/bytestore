# Registration form 

import re 
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
	username = forms.RegexField(regex=r'\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_message=_("Username required, and only alpha characters"))
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=45)), label=_("Email Address))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:	
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The passwords fields do not match."))
		return self.cleaned_data


