from core.test_setup import InitCreateUser
from rest_framework import status


class ProfileAccount(InitCreateUser):
    def test_create_account(self):
        payload = {
            "email": "email@gmacdil.com",
            "password": "Pass24cd.",
            "profile": {
                "establishment_name": "Nome do estabelecimento",
                "tax_document": "02308244550",
                "description": "Descricao do estabelecimento",
                "is_active": False,
                "can_pick_up_in_store": True
            }
        }
        response = self.client.post(
            "/profile/",
            data=payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response=response, text="token", status_code=201)

    def test_get_my_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.get("/my-profile/")
        self.assertContains(response=response, text="id")

    def test_login(self):
        response = self.client.post(
            "/api-token-auth/",
            data={
                "username": "melquiades@gmail.com",
                "password": "melquiades@gmail.com",
            },
        )
        self.assertContains(response=response, text="token")
