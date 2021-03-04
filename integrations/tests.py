import json

from rest_framework import status
from rest_framework.test import APITestCase

from integrations.models import IntegrationData


class IntegrationsTest(APITestCase):
    def test_zapei_integration(self):
        data = json.dumps({
            "leads": [{
                "email": "email@gmail.com",
                "name": "name",
                "personal_phone": "+55 (71) 98836-2338",
            }]
        })
        integration = IntegrationData.objects.create(
            url_sufix="zapei",
            token_zapei="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ikpvc2UgUm9iZXJ0byBBbG1laWRhIiwicm9sZSI6IlB1YmxpY1VzZXIiLCJwcmltYXJ5c2lkIjoiMzg4NiIsImNlcnRzZXJpYWxudW1iZXIiOiI4Njk5ODc0MC1hODI1LTQzMWMtYTUyYi1iYjZkNDcwNzhjNDIiLCJhdXRobWV0aG9kIjoiSldUIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvY291bnRyeSI6IkludmFyaWFudCBDb3VudHJ5IiwiZ3JvdXBzaWQiOiIyMDU3IiwibmJmIjoxNjE0NTQ3NjM2LCJleHAiOjE2MzAwOTk2MzYsImlhdCI6MTYxNDU0NzYzNiwiaXNzIjoiemFwZmFjaWwtYXBpIiwiYXVkIjoiemFwZmFjaWwtY2xpZW50cyJ9.itdOtJ6NBirhFFGB-BQhOUzGXanJuoKB8ymZ1ERtdVw",
        )
        response = self.client.post(
            f"/integracao/{integration.url_sufix}/",
            data=data,
            content_type="application/json"
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_200_OK
        )
