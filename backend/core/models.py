from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel
)

CURRENCIES = [('BTC', ('Bitcoin')),
            ('ETH', ('Ethereum')),
            ('TRX', ('Tron'))]
            

class Contact(
        TimeStampedModel,
        ActivatorModel,
        TitleDescriptionModel,
        Model
):

    class Meta:
        verbose_name_plural = "Contacts"

    email = models.EmailField(verbose_name="Email")
    name = models.CharField(verbose_name="Name", max_length=100)
    message = models.CharField(verbose_name="Message", max_length=100)

    def __str__(self):
        return f'{self.title}'


class Wallet(
        TimeStampedModel,
        ActivatorModel,
        Model
):
        
    class Meta:
        verbose_name_plural = "Wallets"
	
	
    currency = models.CharField(
        max_length=3, verbose_name='currency', default="BTC",choices=CURRENCIES)
    network = models.CharField(
        max_length=255, blank=True, verbose_name='network', default="mainnet")

    def __str__(self):
        return f'{self.id}'


class Address(
        TimeStampedModel,
        ActivatorModel,
        Model
):

    class Meta:
        verbose_name_plural = "Addresses"
    wallet = models.UUIDField(
        max_length=255, verbose_name='wallet_id', null=False, blank=False)
    public_address = models.CharField(
        max_length=255, verbose_name='public_address')
    private_address = models.CharField(
        max_length=255, verbose_name='private_address')

    def __str__(self):
        return f'{self.public_address}'
