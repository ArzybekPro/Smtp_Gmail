
from django.urls import path
from .views import send_mail2

urlpatterns = [
    path('',send_mail2 , name = 'send_mail')
]
