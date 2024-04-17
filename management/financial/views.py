from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import requests
from financial.tasks import add_to_db, create_currency_report



class BankAPI(APIView):

    def get(self, request):
        add_to_db()
        return Response()


class GenerateReportAPI(APIView):

    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        from_currency = request.GET.get('from_currency')
        to_currency = request.GET.get('to_currency')

        create_currency_report.apply_async(args=[start_date, end_date, from_currency, to_currency])

        return Response()
