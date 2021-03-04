import json
import re

import requests
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from integrations.models import RdStationZapei


class RDZapeiIntegrarion(viewsets.ViewSet):

    permission_classes = (AllowAny,)

    def create(self, request, url_sufix=None):
        raw_payload = str(request.body, 'utf-8')
        payload = json.loads(raw_payload)
        leads = payload.get('leads', '')
        for lead in leads:
            email = lead['email']
            name = lead['name']
            personal_phone = re.sub('\W+', '', lead['personal_phone'])
            integration: RdStationZapei = RdStationZapei.objects.get(
                url_sufix=url_sufix
            )
            ZAPEI_HEADERS = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {integration.token_zapei}",
            }
            requests.post(
                "https://api.painel.zapfacil.com/api/leads",
                json={
                    "MetaData": {
                        "Nome": name
                    },
                    "Channel": "Whatsapp",
                    "Contact": {
                        "Phone": personal_phone,
                        "Email": email
                    },
                    "Note": "From Integration"
                },
                headers=ZAPEI_HEADERS
            )

        return Response(status=status.HTTP_200_OK)
