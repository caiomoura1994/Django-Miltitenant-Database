from rest_framework.test import APITestCase

from core.test_setup import InitCreateUser
from core.utils import generate_slug


class TestUtils(InitCreateUser):
    def test_generate_slug(self):
        self.assertNotEqual(generate_slug(self.store), "establishment-name")

    def test_generate_new_slug(self):
        self.assertEqual(generate_slug(self.store, "slug-novo"), "slug-novo")
