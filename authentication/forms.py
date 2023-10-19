from django import forms
from .models import CustomUser
from django.contrib import messages
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=30, 
        required=True, 
        error_messages={
            'required': 'Please enter your username.',
            'max_length': 'Username should be 30 characters or less.',
            'min_length': 'Username should be greater than 3 characters.'
        }
    )
    password = forms.CharField(
        widget = forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        username, password = cleaned_data.get('username'), cleaned_data.get('password')
        user = CustomUser.objects.get_object_or_none(username=username)
        if not user:
            raise ValidationError(f'Username {username} does not exists!')
        if not user.check_password(password):
            raise ValidationError('Entered password is wrong!')
        


class SignUpForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    confirm_password = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'profile_photo', 'password']

    widget = {
        'password': forms.PasswordInput()
    }

    def validate_username(self, username):
        if CustomUser.objects.get_object_or_none(username=username):
            raise ValidationError('{username} already exists!')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        password, confirm_password = cleaned_data.get('password'), cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')

    def save(self):
        user = super().save()
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user
