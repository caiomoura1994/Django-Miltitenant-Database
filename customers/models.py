from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(blank=True, default=None, null=True)
    on_trial = models.BooleanField(blank=True, default=None, null=True)
    created_on = models.DateField(auto_now_add=True)
