from django.urls import path

from integrations.views import RDZapeiIntegrarion

urlpatterns = [
    path('rd-zapei/<url_sufix>/',
         RDZapeiIntegrarion.as_view({'post': 'create'}))
]
