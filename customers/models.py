from django.contrib.auth.models import User
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    name = models.CharField(max_length=100)
    paid_until = models.DateField(blank=True, default=None, null=True)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    stripe_customer_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        default=None
    )

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
