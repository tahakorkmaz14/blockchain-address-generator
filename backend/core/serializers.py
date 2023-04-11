from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


class ContactSerializer(serializers.ModelSerializer):

    name = CharField(required=True)
    message = CharField(required=True)
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'email',
            'message'
        )


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'currency',
            'network'
        )


class AddressSerializer(serializers.ModelSerializer):
    wallet = serializers.UUIDField()

    class Meta:
        model = models.Address
        fields = (
            'wallet',
            'public_address',
            'private_address'
        )
