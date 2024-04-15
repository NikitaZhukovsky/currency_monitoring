from rest_framework import serializers
from financial.models import Currency, ExchangesRate, Subscription
from datetime import date


class CurrencySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ExchangesRate
        fields = ('currency_from', 'currency_to', 'exchange_rate')
