import json
from profile.models import Profile

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from store.models import Store

from .serializers import (CheckUsernameProfileSerializer, ProfileSerializer,
                          RegisterProfileSerializer, UpdateProfileSerializer)
from .utils import (generate_random_password, is_valid_password,
                    send_user_new_password_message, send_user_support_message)


@api_view(['GET'])
def my_profile(request):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_204_NO_CONTENT)
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(profile)
    return Response(status=status.HTTP_200_OK,  data=serializer.data)


@api_view(['POST'])
def send_support_message(request):
    raw_payload = str(request.body, 'utf-8')
    payload = json.loads(raw_payload)
    full_name = payload.get('full_name', '')
    email = payload.get('Email', '')
    telephone = payload.get('telephone', '')
    subject = payload.get('subject', '')
    message = payload.get('message', '')

    ret = send_user_support_message(
        full_name,
        email,
        telephone,
        subject,
        message,
    )
    if ret:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # ---
        token, created = Token.objects.get_or_create(user=user)
        # ---
        return Response({
            'token': token.key,
        })


class UserChangePasswordViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def create(self, request):
        if not 'username' in request.data:
            raise ValidationError(
                'Identificador do usuário não informado.', 400)
        if not 'old_password' in request.data:
            raise ValidationError('Senha antiga não informada.', 400)
        if not 'new_password' in request.data:
            raise ValidationError('Nova senha não informada.', 400)
        if not 'new_password_confirmation' in request.data:
            raise ValidationError(
                'Confirmação da nova senha não informada.', 400)
        new_password = request.data['new_password']
        new_password_confirmation = request.data['new_password_confirmation']
        if not is_valid_password(new_password, new_password_confirmation):
            raise ValidationError(
                'A nova senha e sua confirmação devem ser iguais e conter, no mínimo, 6 caracteres e uma letra maiúscula.',
                400
            )
        user = User.objects.get(username__exact=request.data['username'])
        if not user:
            raise ValidationError(
                'Usuário não encontrado para o e-mail informado.', 404)
        if not user.check_password(request.data['old_password']):
            raise ValidationError('Senha atual informada está incorreta.', 400)
        user.set_password(new_password)
        user.save()
        return Response('Senha alterada com suucesso.', status=200)


class UserForgotPasswordViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny,)

    def create(self, request):
        if not 'username' in request.data:
            raise ValidationError(
                'Identificador do usuário não informado.', 400)
        try:
            user = User.objects.get(username__exact=request.data['username'])
        except ObjectDoesNotExist:
            raise NotFound('E-mail informado não está cadastrado.')
        new_password = generate_random_password()
        user.set_password(new_password)
        user.save()
        send_user_new_password_message(
            Profile.objects.get(user=user), new_password)
        return Response('Nova senha enviada para {}.'.format(request.data['username']), status=200)


class UserCheckUsernameViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return CheckUsernameProfileSerializer

    def create(self, request):
        if not 'email' in request.data:
            raise ValidationError('Email não informado.', 400)
        try:
            User.objects.get(username__exact=request.data['email'])
        except ObjectDoesNotExist:
            raise NotFound('E-mail informado não está cadastrado.')
        return Response('E-mail informado JÁ está cadastrado.', status=200)


class ProfileViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterProfileSerializer
        if self.action == 'partial_update':
            return UpdateProfileSerializer
        if self.action == 'update':
            return UpdateProfileSerializer
        return ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super(ProfileViewSet, self).get_permissions()

    def create(self, request, **kwargs):
        serializer = RegisterProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            new_profile = Profile.objects.get(
                user__email=data["email"]
            )
            token, created = Token.objects.get_or_create(
                user=new_profile.user
            )
            data['token'] = None
            if created:
                data['token'] = token.key
            # send_welcome_message(new_profile.establishment_name, data["email"])

        return Response(data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        serializer = UpdateProfileSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profile: Profile = Profile.objects.get(pk=pk)
            for (key, value) in request.data['profile'].items():
                setattr(profile, key, value)
            profile.save()
            store: Store = profile.store
            for (key, value) in request.data['store'].items():
                setattr(store, key, value)

            return Response(serializer.data, status=status.HTTP_200_OK)
