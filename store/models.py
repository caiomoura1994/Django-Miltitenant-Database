from profile.models import Profile

from core.utils import generate_slug
from django.db import models
from django.utils.html import format_html


class Store(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="stores"
    )
    establishment_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, verbose_name='Descrição')
    photo = models.CharField(max_length=256, null=True, blank=True)
    is_active = models.BooleanField(null=True, default=False)
    can_pick_up_in_store = models.BooleanField(null=True, default=False)
    slug = models.SlugField(
        null=True,
        default=None,
        max_length=50,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class Category(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, slug:{self.slug}'


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(decimal_places=2, max_digits=30)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    photo = models.CharField(max_length=256, null=True, blank=True)
    slug = models.SlugField(
        null=True,
        default=None,
        max_length=50,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        if not self.store:
            return ""
        return generate_slug(self, f'{self.store.name} {self.name}')

    def __str__(self):
        return f'{self.name}, slug:{self.slug}'


class Address(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=100)
    public_place = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    complement = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class OpeningHour(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    start_hour = models.CharField(max_length=100)
    end_hour = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=100)
