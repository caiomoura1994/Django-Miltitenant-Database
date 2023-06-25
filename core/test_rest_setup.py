from django.core import mail
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from rest_framework.test import ForceAuthClientHandler


class MultiTenantAPIClient(TenantClient):
    """
    This is a combination of the django-tenants TenantClient and
    DRFs APIClient.
    """

    def __init__(self, tenant, enforce_csrf_checks=False, **defaults):
        super(MultiTenantAPIClient, self).__init__(tenant, **defaults)
        self.handler = ForceAuthClientHandler(enforce_csrf_checks)
        self._credentials = {}

    def credentials(self, **kwargs):
        """
        Sets headers that will be used on every outgoing request.
        """
        self._credentials = kwargs

    def force_authenticate(self, user=None, token=None):
        """
        Forcibly authenticates outgoing requests with the given
        user and/or token.
        """
        self.handler._force_user = user
        self.handler._force_token = token
        if user is None:
            self.logout()  # Also clear any possible session info if required

    def logout(self):
        self._credentials = {}

        # Also clear any `force_authenticate`
        self.handler._force_user = None
        self.handler._force_token = None

        if self.session:
            super(MultiTenantAPIClient, self).logout()


class MultiTenantAPITestCase(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        """
        TenantTestCase doesn't call super().setUpClass() and 
        TestCase.setUpClass() is responsible for calling cls.setUpTestData()
        so we'll need to call it ourselves.
        """
        super().setUpClass()
        try:
            cls.setUpTestData()
        except Exception:
            cls._rollback_atomics(cls.cls_atomics)
            raise

    def _pre_setup(self):
        """
        super()._pre_setup() will throw an error if we set the client_class
        on the class level because it doesn't know about the tenant argument.

        That said, we still need to set it because it'll cause errors on the
        teardown if we don't. So we'll call super()._pre_setup() first, then
        define it and self.client.
        """
        super()._pre_setup()
        self.client_class = MultiTenantAPIClient
        self.client = self.client_class(tenant=self.tenant)
