from django.contrib import admin
from financial.models import Currency, ExchangesRate, Subscription


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangesRate)
admin.site.register(Subscription)