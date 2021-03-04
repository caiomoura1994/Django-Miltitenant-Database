import json

from rest_framework import status
from rest_framework.test import APITestCase

from integrations.models import RdStationZapei


class IntegrationsTest(APITestCase):
    def test_zapei_integration(self):
        data = json.dumps({
            "leads": [{
                "email": "email@gmail.com",
                "name": "name",
                "personal_phone": "+55 (71) 98836-2338",
            }]
        })
        integration = RdStationZapei.objects.create(
            url_sufix="zapei-test-testando",
            token_zapei="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IkNhaW8gTW91cmEiLCJyb2xlIjoiUHVibGljVXNlciIsInByaW1hcnlzaWQiOiIxNjIzIiwiY2VydHNlcmlhbG51bWJlciI6IjZmYTY4YTJhLTJjZTUtNDA3Zi05YmEzLWI4YTNhMTI3YWZhYyIsImF1dGhtZXRob2QiOiJKV1QiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9jb3VudHJ5IjoiSW52YXJpYW50IENvdW50cnkiLCJncm91cHNpZCI6IjI1NDciLCJuYmYiOjE2MTQ4MzEyMzUsImV4cCI6MTYzMDM4MzIzNSwiaWF0IjoxNjE0ODMxMjM1LCJpc3MiOiJ6YXBmYWNpbC1hcGkiLCJhdWQiOiJ6YXBmYWNpbC1jbGllbnRzIn0.olKuR0xrw4Ff9yJKFLGKP3AvOiolf4RWmZjCZuLGtIk",
        )
        response = self.client.post(
            f"/integrations/rd-zapei/{integration.url_sufix}/",
            data=data,
            content_type="application/json"
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_200_OK
        )
