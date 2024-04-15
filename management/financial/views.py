from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import requests
from financial.tasks import add_to_db


class BankAPI(APIView):

    def get(self, request):
        add_to_db()
        return Response()

