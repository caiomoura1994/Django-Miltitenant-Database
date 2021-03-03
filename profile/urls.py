from profile.views import (CustomAuthToken, ProfileViewSet,
                           UserChangePasswordViewSet, UserCheckUsernameViewSet,
                           UserForgotPasswordViewSet, my_profile,
                           send_support_message)

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    url(r'^contact-us/', send_support_message),
    url(r'^my-profile/', my_profile),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^check-username/',
        UserCheckUsernameViewSet.as_view({'post': 'create'})),
    url(r'profile/change_password/',
        UserChangePasswordViewSet.as_view({'post': 'create'}), name='user-change-password'),
    url(r'profile/forgot_password/',
        UserForgotPasswordViewSet.as_view({'post': 'create'}), name='user-forgot-password'),
    url(r'^', include(router.urls)),
]
