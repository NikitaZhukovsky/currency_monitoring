from celery import shared_task
import datetime
import time
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
import requests
from financial.models import ExchangesRate, Currency
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from io import BytesIO


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


@shared_task
def create_currency_report(start_date, end_date, from_currency, to_currency):
    exchange_rate_data = ExchangesRate.objects.filter(currency_from=from_currency, currency_to=to_currency,
                                                      created_date__range=[start_date, end_date]).order_by('created_date').values('created_date', 'exchange_rate')

    dates = [data['created_date'] for data in exchange_rate_data]
    rates = [data['exchange_rate'] for data in exchange_rate_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')

    response = BytesIO()
    plt.savefig(response, format='pdf')
    plt.close()

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 700, f'Currency Exchange Report {from_currency} to {to_currency} from {start_date} to {end_date}')
    pdf.save()

    with open(f'currency_report_{from_currency}_to_{to_currency}_{start_date}_{end_date}.pdf', 'wb') as f:
        f.write(response.getvalue())
