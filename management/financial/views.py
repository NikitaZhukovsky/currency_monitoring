from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import requests


class BankAPI(APIView):

    def get(self, request):
        data = requests.get('https://api.nbrb.by/exrates/rates?periodicity=0')
        for item in data.json():
            if item['Cur_ID'] == 431:
                print(item['Cur_Abbreviation'], item['Cur_OfficialRate'])



        return Response()

