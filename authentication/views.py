from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
# from django.views.generic.base import 
from django.conf import settings

from .forms import (
    LoginForm,
    SignUpForm
)

from .models import (
    CustomUser
)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        user = authenticate(
            self.request, 
            username=cleaned_data.get('username'), 
            password=cleaned_data.get('password')
        )

        login(self.request, user)
        return super().form_valid(form=form)



class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('authentication:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form=form)



        
