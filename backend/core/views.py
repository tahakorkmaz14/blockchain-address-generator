from json import JSONDecodeError
from django.http import JsonResponse

from .models import Address, Wallet
from .serializers import ContactSerializer, WalletSerializer, AddressSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .address import GenerateAddress
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires. Later Stages: Will going to be used for login purposes and customer storing
    """
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)


class WalletAPIView(views.APIView):

    """
    An APIView for creating new blockchain addresses. Can be used for ETH, BTC and TRX networks.
    """

    serializer_class = WalletSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = WalletSerializer(data=data)
            # and data.get("currency") in {'BTC', 'ETH', 'TRX'}:
            if serializer.is_valid(raise_exception=True):
                wallet = serializer.save()
                generated = GenerateAddress(currency=data.get(
                    'currency'), network=data.get('network'))
                generated["wallet"] = wallet.id
                address = AddressSerializer(data=generated)
                if address.is_valid(raise_exception=True):
                    address.save()
                    return Response(address.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)


@api_view(['GET'])
def getAddress(request, pk):
    """
    An APIView for getting a specific blockchain address and secretkey
    """

    address = Address.objects.get(id=pk)
    wallet = Wallet.objects.get(id=address.wallet)
    data = {"id": pk,
            "public_address": address.public_address,
            "private_key": address.private_address,
            "currency": wallet.currency,
            "network": wallet.network}

    return Response(data=data)


@api_view(['GET'])
def listAddress(request):
    """
    An APIView for getting all stored addresses. Later stages: Only be used by admins at 
    """

    addresses = Address.objects.all()
    wallets = Wallet.objects.all()
    data = []
    for address in addresses:
        wallet = Wallet.objects.get(id=address.wallet)
        data.append({"id": address.id,
                     "public_address": address.public_address,
                     "private_key": address.private_address,
                     "currency": wallet.currency,
                     "network": wallet.network})

    return Response(data=data)
