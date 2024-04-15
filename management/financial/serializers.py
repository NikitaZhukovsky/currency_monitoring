from rest_framework import serializers
from financial.models import Currency, ExchangesRate, Subscription
from datetime import date


class CurrencySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'description')