from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html

from .utils import generate_slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment_name = models.CharField(
        max_length=100, verbose_name='Nome do Estabelecimento')
    tax_document = models.CharField(max_length=100, verbose_name='CPF ou CNPJ')
    description = models.CharField(max_length=100, verbose_name='Descrição')
    photo = models.CharField(max_length=256, null=True, blank=True)
    is_active = models.BooleanField(
        null=True, default=False, verbose_name='Está ativo')
    can_pick_up_in_store = models.BooleanField(
        null=True, default=False, verbose_name='Pode retirar na loja')
    slug = models.SlugField(
        null=True,
        default=None,
        max_length=50,
        unique=True
    )

    def photo_mini(self):
        if not self.photo:
            return format_html('Sem foto de perfil')
        return format_html(
            '''<img src="{0}" style="height: 7vh; border: 0;"/>''',
            self.photo
        )
    photo_mini.allow_tags = True
    photo_mini.short_description = "Foto de perfil"

    def slugify_function(self, content):
        return generate_slug(self, self.establishment_name)

    def __str__(self):
        return f'{self.establishment_name}, slug:{self.slug}'

    # def __init__(self, *args, **kwargs):
    #     super(Profile, self).__init__(*args, **kwargs)
    #     self.old_is_active = self.is_active
