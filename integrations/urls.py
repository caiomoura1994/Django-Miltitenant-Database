from django.conf.urls import url

from integrations.views import RDZapeiIntegrarion

urlpatterns = [
    url(r'rd-zapei/(?P<url_sufix>[a-z]+)',
        RDZapeiIntegrarion.as_view({'post': 'create'}))
]
