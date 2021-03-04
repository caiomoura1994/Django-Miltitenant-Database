from django.conf.urls import url

from integrations.views import zapei_integration

urlpatterns = [
    url(r'^integracao/(?P<url_sufix>[a-z]+)/', zapei_integration)
]
