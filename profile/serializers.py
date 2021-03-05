from core.utils import generate_slug
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from store.models import Store
from store.serializers import StoreSerializer

from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Client
        depth = 1
        exclude = ('user', )

    def get_email(_, obj):
        try:
            return obj.user.email
        except Exception:
            return None


class RegisterSerializer(serializers.ModelSerializer):
    client = ClientSerializer(required=True)
    store = StoreSerializer(required=True)

    class Meta:
        model = User
        fields = ("email", "password", "client", "store")

    def create(_, validated_data):
        email = validated_data['email']
        if User.objects.filter(username=email).exists():
            raise ValidationError("Email ja cadastrado")

        password = validated_data['password']
        user = User(email=email, username=email)
        user.set_password(password)
        user.save()
        client_data = validated_data['client']
        store_data = validated_data['store']
        client: Client = Client.objects.create(user=user, **client_data)
        store: Store = Store.objects.create(client=client, **store_data)
        store.slug = generate_slug(store)
        validated_data['store']['slug'] = store.slug
        validated_data['password'] = None
        store.save()
        client.save()
        return validated_data
