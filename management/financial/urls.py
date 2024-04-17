from django.urls import path
from financial.views import BankAPI, GenerateReportAPI

urlpatterns = [
    path('currency/', BankAPI.as_view(), name='currency'),
    path('create_report/', GenerateReportAPI.as_view(), name='create_report')
]
