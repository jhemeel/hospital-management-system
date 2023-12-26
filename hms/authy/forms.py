from allauth.account.forms import SignupForm
from django import forms
from .utils import DivErrorList

class CustomSignupForm(SignupForm):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(
        attrs={'id': 'name', 'class': 'name'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'id': 'email', 'class': 'email'}))
    
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
    
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        name = self.cleaned_data['name']
        email = self.cleaned_data['email']

        user.name = name
        user.email = email

        user.save()
        return user
    
    
