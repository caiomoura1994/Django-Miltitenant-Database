from profile.models import Client

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from store.models import Store


class InitCreateUser(APITestCase):
    def setUp(self):
        self.user: User = User.objects.create_user(
            'melquiades@gmail.com',
            'melquiades@gmail.com',
            'melquiades@gmail.com'
        )
        self.client_instance = Client.objects.create(
            user=self.user,
            tax_document="00000000000",
        )
        self.store = Store.objects.create(
            client=self.client_instance,
            establishment_name="establishment_name",
            description="description",
            is_active=True,
            can_pick_up_in_store=True,
            slug="slug",
        )
        self.token = Token.objects.create(user=self.user)
