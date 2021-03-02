from profile.models import Profile

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class InitCreateUser(APITestCase):
    def setUp(self):
        self.user: User = User.objects.create_user(
            'melquiades@gmail.com',
            'melquiades@gmail.com',
            'melquiades@gmail.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            establishment_name="establishment_name",
            tax_document="00000000000",
            description="description",
            is_active=True,
            can_pick_up_in_store=True,
            slug="slug",
        )
        self.token = Token.objects.create(user=self.user)
