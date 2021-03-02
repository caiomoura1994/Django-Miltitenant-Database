from django.conf import settings
from django.contrib import admin

from .models import Profile

admin.site.site_header = "Zapei Loja Admin"


class CSSAdminMixin(object):
    class Media:
        css = {
            'all': ('admin/css/personal.css',),
        }


NORMAL_USER_FIELDS = [
    'establishment_name',
    'tax_document',
    'description',
    'photo',
    'is_active',
    'can_pick_up_in_store',
    'slug',
]


class ProfileAdmin(admin.ModelAdmin, CSSAdminMixin):
    list_filter = (
        'establishment_name',
        'is_active',
        'slug',
    )
    list_display = (
        'establishment_name',
        'is_active',
        'slug',
    )
    search_fields = ('establishment_name',)

    # def get_readonly_fields(self, request, obj=None):
    #     return NORMAL_USER_FIELDS

    def get_fields(self, request, obj=None):
        new_fields = ['is_active']
        for field in NORMAL_USER_FIELDS:
            new_fields.append(field)
        return new_fields


admin.site.register(Profile, ProfileAdmin)
