from core.utils import generate_slug
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from store.models import Store
from store.serializers import StoreSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        depth = 1
        exclude = ('user', )

    def get_email(_, obj):
        try:
            return obj.user.email
        except Exception:
            return None


class RegisterProfileSerializer(serializers.Serializer):
    profile = ProfileSerializer(required=True)
    store = StoreSerializer(required=True)
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(_, validated_data):
        email = validated_data['email']
        if User.objects.filter(username=email).exists():
            raise ValidationError("Email ja cadastrado")

        password = validated_data['password']
        user = User(email=email, username=email)
        user.set_password(password)
        user.save()
        profile_data = validated_data['profile']
        store_data = validated_data['store']
        profile: Profile = Profile.objects.create(user=user, **profile_data)
        store: Store = Store.objects.create(profile=profile, **store_data)
        store.slug = generate_slug(store)
        validated_data['store']['slug'] = store.slug
        validated_data['password'] = None
        store.save()
        profile.save()
        return validated_data


class UpdateProfileSerializer(serializers.Serializer):
    profile = ProfileSerializer(required=False)
    store = StoreSerializer(required=False)
