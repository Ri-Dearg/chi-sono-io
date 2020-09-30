from django.urls import path
from .views import CreateEmailView, AboutTemplate

urlpatterns = [
    path('contact/', CreateEmailView.as_view(), name='email-form'),
    path('about/', AboutTemplate.as_view(), name='about'),
]
