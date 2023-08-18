from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserAddress
from django.db import transaction

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = [
            'street_address',
            'city',
            'postal_code',
            'country'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email',
                  'first_name', 
                  'last_name', 
                  'password1', 
                  'password2'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        



class UserChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields