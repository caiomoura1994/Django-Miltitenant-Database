import json
from profile.models import Profile
from unittest.mock import patch

from rest_framework import status

from core.test_setup import InitCreateUser
from store.models import Store


class ProfileAccount(InitCreateUser):
    def test_create_account(self):
        payload = {
            "email": "email@gmacdil.com",
            "password": "Pass24cd.",
            "profile": {
                "tax_document": "02308244550",
            },
            "store": {
                "establishment_name": "Nome do estabelecimento",
                "description": "Descricao do estabelecimento",
                "is_active": False,
                "can_pick_up_in_store": True
            }
        }
        response = self.tenant_client.post(
            "/profile/",
            data=payload,
            format="json",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response=response, text="token", status_code=201)

        response = self.tenant_client.post(
            "/profile/",
            data=payload,
            format="json",
            content_type="application/json"
        )
        self.assertContains(response=response, text="", status_code=400)

    def test_update_profile(self):
        payload = {
            "profile": {
                "tax_document": "0230824455"
            },
            "store": {
                "establishment_name": "novo nome",
                "description": "description",
            },
        }
        self.tenant_client.force_authenticate(self.user, self.token)
        response = self.tenant_client.patch(
            f"/profile/{self.profile_instance.pk}/",
            data=payload,
            format="json",
            content_type="application/json"
        )
        profile: Profile = Profile.objects.get(pk=self.profile_instance.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "0230824455")
        self.assertEqual(profile.tax_document, "0230824455")

    def test_get_my_profile(self):
        response_without_auth = self.tenant_client.get("/my-profile/")
        self.assertContains(
            response=response_without_auth,
            text="",
            status_code=status.HTTP_204_NO_CONTENT
        )

        self.tenant_client.force_authenticate(self.user, self.token)
        response = self.tenant_client.get("/my-profile/")
        self.assertContains(response=response, text="id")

    def test_login(self):
        response = self.tenant_client.post(
            "/api-token-auth/",
            data={
                "username": "melquiades@gmail.com",
                "password": "melquiades@gmail.com",
            },
        )
        self.assertContains(response=response, text="token")

    @patch('profile.views.send_user_support_message')
    def test_send_support_message(self, send_user_support_message):
        data = json.dumps({
            "full_name": "full_name",
            "email": "email",
            "telephone": "telephone",
            "subject": "subject",
            "message": "message"
        })
        send_user_support_message.return_value = True
        response = self.tenant_client.post(
            "/contact-us/",
            data=data,
            content_type="application/json"
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_204_NO_CONTENT
        )

        send_user_support_message.return_value = False
        response = self.tenant_client.post(
            "/contact-us/",
            data=data,
            content_type="application/json"
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    def test_check_user_name(self):
        response = self.tenant_client.post(
            "/check-username/",
            data={"email": "naoexiste@gmail.com"}
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_404_NOT_FOUND
        )
        response = self.tenant_client.post(
            "/check-username/",
            data={"email": "melquiades@gmail.com"}
        )
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_200_OK
        )
        response = self.tenant_client.post("/check-username/", data={})
        self.assertContains(
            response=response,
            text="",
            status_code=status.HTTP_400_BAD_REQUEST
        )
