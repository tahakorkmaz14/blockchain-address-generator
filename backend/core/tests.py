from . models import Contact, Address, Wallet
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


class ContactTestCase(APITestCase):

    """
    Test suite for Contact, Address and Wallet
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Billy Smith",
            "message": "This is a test message",
            "email": "billysmith@test.com"
        }
        self.url = "/contact/"

    def test_create_contact(self):
        '''
        test ContactViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().title, "Billy Smith")

    def test_create_contact_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_name_equals_blank(self):
        '''
        test ContactViewSet create method when name is blank
        '''
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_message(self):
        '''
        test ContactViewSet create method when message is not in data
        '''
        data = self.data
        data.pop("message")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_message_equals_blank(self):
        '''
        test ContactViewSet create method when message is blank
        '''
        data = self.data
        data["message"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_email(self):
        '''
        test ContactViewSet create method when email is not in data
        '''
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_equals_blank(self):
        '''
        test ContactViewSet create method when email is blank
        '''
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_equals_non_email(self):
        '''
        test ContactViewSet create method when email is not email
        '''
        data = self.data
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class AddressTestCase(APITestCase):

    """
    Test suite for Address
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {"currency":"BTC", "network":"mainnet"}
        self.url = "/generate-address/"

    def test_create_address(self):
        '''
        test AddressViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Address.objects.get().wallet, Wallet.objects.get().id)

    def test_address_without_currency(self):
        '''
        test addressViewSet create method when currency is not in data
        '''
        data = self.data
        data.pop("currency")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_address_without_network(self):
        '''
        test addressViewSet create method when network is not in data default mainnet
        '''
        data = self.data
        data.pop("network")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_address_with_unsupported_currency_network(self):
        '''
        test addressViewSet create method when name is not in data
        '''
        data = self.data
        data["network"]="SOL"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)