from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ValidationError

from .models import Profile
from .utils import generate_slug


class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        depth = 1
        exclude = ('user', )

    def get_email(self, obj):
        try:
            return obj.user.email
        except Exception:
            return None


class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ("email", "password", "profile")

    def create(self, validated_data):
        email = validated_data['email']
        if User.objects.filter(username=email).exists():
            raise ValidationError("Email ja cadastrado")

        password = validated_data['password']
        user = User(
            email=email,
            username=email
        )
        user.set_password(password)
        user.save()
        profile_data = validated_data['profile']
        profile: Profile = Profile.objects.create(user=user, **profile_data)
        profile.slug = generate_slug(profile)
        validated_data['profile']['slug'] = profile.slug
        validated_data['password'] = None
        profile.save()
        return validated_data
