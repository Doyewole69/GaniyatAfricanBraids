from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView, RedirectView,CreateView
from .forms import UserRegistrationForm, UserChangeForm, UserAddressForm
from django.contrib import messages

User = get_user_model()


class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user_registration.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse_lazy('home')
            )
        return super().dispatch(request, *args, **kwargs)
    
    def post (self, request, *args, **kwargs):
       registration_form = UserRegistrationForm(self.request.POST) 
       address_form = UserAddressForm(self.request.POST)
       
       if registration_form.is_valid() and address_form.is_valid():
           user = registration_form.save()
           user_address = address_form.save(commit=False)
           user_address.user = user
           user_address.save()
           
           login(self.request, user)
           messages.success(self.request,
                            (
                                f'Welcome to Ganiyats African Braids {user.first_name} '
                            ))
           return HttpResponseRedirect(reverse_lazy('home'))
       
       return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                address_form=address_form
                
            )
        )
        
    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = UserAddressForm()
            
        return super().get_context_data(**kwargs)
    
    
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = False
    
    
class UserLogoutView(LogoutView):
    pattern_name = 'home'
    
    def get_redirected_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirected_url(*args, **kwargs)
    
    
def aboutus(request):
    return render(request, 'aboutus.html')
    
           
class HomeView(TemplateView):
    template_name = 'index.html'
    
   
