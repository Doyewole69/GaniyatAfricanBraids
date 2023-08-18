from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserAddress
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    ordering = ('email',)
    
    
admin.site.register(User, UserAdmin)
admin.site.register(UserAddress)