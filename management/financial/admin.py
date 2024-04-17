from django.contrib import admin
from financial.models import Currency, ExchangesRate, Subscription


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


class ExchangesRateAdmin(admin.ModelAdmin):
    list_display = ('currency_from', 'currency_to', 'exchange_rate', 'created_date')
    search_fields = ('currency_from', 'currency_to', 'exchange_rate', 'created_date')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangesRate, ExchangesRateAdmin)
admin.site.register(Subscription)