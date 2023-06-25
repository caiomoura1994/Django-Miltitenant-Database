import logging
from profile.models import Profile

from django.contrib.auth.models import User
from django_tenants.utils import tenant_context
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from core.test_rest_setup import MultiTenantAPIClient, MultiTenantAPITestCase
from store.models import Store


class InitCreateUser(APITestCase, MultiTenantAPITestCase):
    def setUp(self):
        super().setUp()
        logging.getLogger('django.request').setLevel(logging.CRITICAL)
        self.tenant_client = MultiTenantAPIClient(self.tenant)
        with tenant_context(self.tenant):
            # self.tenant_client.login()
            self.user: User = User.objects.create_user(
                'melquiades@gmail.com',
                'melquiades@gmail.com',
                'melquiades@gmail.com'
            )
            self.profile_instance = Profile.objects.create(
                user=self.user,
                tax_document="00000000000",
            )
            self.store: Store = Store.objects.create(
                profile=self.profile_instance,
                establishment_name="Establishment Name",
                description="description",
                is_active=True,
                can_pick_up_in_store=True,
                slug="establishment-name",
            )
            self.token = Token.objects.create(user=self.user)
