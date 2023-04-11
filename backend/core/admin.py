from django.contrib import admin
from .models import Contact, Address, Wallet


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'public_address', 'private_address')


@admin.register(Wallet)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'network')
