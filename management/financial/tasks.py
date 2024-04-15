from celery import shared_task
import datetime
import time
import datetime
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
import requests
from financial.models import ExchangesRate, Currency

@shared_task()
def add_to_db():
    data = requests.get('https://api.nbrb.by/exrates/rates?periodicity=0')
    for item in data.json():
        if item['Cur_ID'] == 431:
            currency = Currency.objects.filter(name=item['Cur_Abbreviation']).first()
            currency_bun = Currency.objects.filter(name='BYN').first()
            ExchangesRate.objects.create(currency_from=currency, to_currency=currency_bun,
                                         exchange_rate=item['Cur_OfficialRate'])
        if item['Cur_ID'] == 451:
            currency = Currency.objects.filter(name=item['Cur_Abbreviation']).first()
            currency_bun = Currency.objects.filter(name='BYN').first()
            ExchangesRate.objects.create(currency_from=currency, to_currency=currency_bun,
                                         exchange_rate=item['Cur_OfficialRate'])
        if item['Cur_ID'] == 456:
            currency = Currency.objects.filter(name=item['Cur_Abbreviation']).first()
            currency_bun = Currency.objects.filter(name='BYN').first()
            ExchangesRate.objects.create(currency_from=currency, to_currency=currency_bun,
                                         exchange_rate=item['Cur_OfficialRate'])
    return 'Success'


