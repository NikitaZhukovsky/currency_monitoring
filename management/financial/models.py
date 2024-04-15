from django.db import models
from users.models import CustomUser


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.code}'

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class ExchangesRate(models.Model):
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_to')
    created_date = models.DateField()

    class Meta:
        verbose_name = 'Exchanges Rate'
        verbose_name_plural = 'Exchanges Rates'


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    notification = models.CharField(max_length=255)
    is_paid = models.BooleanField()
