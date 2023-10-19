from django.urls import path
from .views import LoginView, SignUpView


app_name = 'authentication'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup')
]