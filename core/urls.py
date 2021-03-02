"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from profile.views import (CustomAuthToken, ProfileViewSet,
                           UserChangePasswordViewSet,
                           UserForgotPasswordViewSet, my_profile,
                           send_support_message)

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^contact-us/', send_support_message),
    url(r'^my-profile/', my_profile),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'profile/change_password/',
        UserChangePasswordViewSet.as_view({'post': 'create'}), name='user-change-password'),
    url(r'profile/forgot_password/',
        UserForgotPasswordViewSet.as_view({'post': 'create'}), name='user-forgot-password'),
    path('admin/', admin.site.urls),
    # path('tinymce/', include('tinymce.urls')),
    url(r'^', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
