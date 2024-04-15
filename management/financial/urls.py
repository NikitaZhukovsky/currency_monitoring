from django.urls import path
from financial.views import BankAPI

urlpatterns = [
    path('currency/', BankAPI.as_view(), name='currency'),
]