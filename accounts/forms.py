# Registration form 
import re 
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class OwnerMixin(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('is_customer',)
		widgets = {
			'is_customer': forms.CheckboxInput({'class': 'form-control'}),
		}

class RegistrationForm(OwnerMixin, UserCreationForm):
	first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.RegexField(regex=r'\w+$', widget=forms.TextInput(attrs={'required':True, 'max_length':30, 'class':'form-control'}), label=_("Username"), error_message=_("Username required, and only alpha characters"))
	email = forms.EmailField(widget=forms.TextInput(attrs={'required':True, 'max_length':45, 'class': 'form-control'}), label=_("Email Address"))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required':True, 'max_length':30, 'render_value':False, 'class':'form-control'}), label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required':True, 'max_length':30, 'render_value':False, 'class':'form-control'}), label=_("Password (again)"))

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:	
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The passwords fields do not match."))
		return self.cleaned_data


"""class StoreOwnerRegistrationForm(RegistrationForm):
	is_owner = forms.BooleanField"""