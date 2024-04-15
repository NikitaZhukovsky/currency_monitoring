from django.contrib import admin
from financial.models import Currency, ExchangesRate, Subscription


admin.site.register(Currency)
admin.site.register(ExchangesRate)
admin.site.register(Subscription)