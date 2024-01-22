"""
_summary_
Create a form for the user registration
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, ContactModel, NewsLetter


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required', required=True)
    
    class Meta:
        model = User
        fields = (
			'username',
			'email',
			'password1',
			'password2'
		)
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        for field_name in [
			'username',
			'email',
			'password1',
			'password2'
		]:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
            
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



# user account
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
			'username',
			'email',
			'first_name',
			'last_name'
		)
        
        
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address',)
        
        
# contact page
class ContactProfile(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = (
			'name',
			'subject',	
			'email',
			'phone',
			'message'
		)



class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email', )