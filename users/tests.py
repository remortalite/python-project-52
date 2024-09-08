from django.test import TestCase
from django.urls import reverse
import logging

from users.models import User

logger = logging.getLogger(__name__)


class UsersViewTest(TestCase):
    fixtures = ["sample.json"]

    def test_status_and_column_name(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"test_user", response.content)


class TestUserFormView(TestCase):
    fixtures = ["sample.json"]

    def setUp(self):
        self.user = User.objects.get(username="test_user")

    def test_post(self):
        self.client.post(reverse("users_create"),
                         data={"username": "test_user_post",
                               "password1": "test_user_post",
                               "password2": "test_user_post"}
                         )
        user = User.objects.get(username="test_user_post")
        self.assertEqual("test_user_post", user.username)

    def test_update_unauthorized(self):
        response = self.client.get(reverse("users_update",
                                           kwargs={"pk": self.user.id}))
        self.assertEqual(response.status_code, 302)

    def test_update_authorized(self):
        self.client.login(username="test_user",
                          password="test_password")
        response = self.client.get(reverse("users_update",
                                           kwargs={"pk": self.user.id}))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test_user", response.content)

        self.client.post(reverse("logout"))

        response = self.client.get(reverse("users_update",
                                           kwargs={"pk": self.user.id}))
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        self.client.login(username="test_user",
                          password="test_password")
        response = self.client.post(reverse("users_delete",
                                    kwargs={"pk": self.user.id}))
        self.assertEqual(response.status_code, 302)

        self.client.logout()

        # create new unbounded user
        user = User.objects.create_user(username="test_user_delete",
                                        password="test_password_delete")
        self.client.login(username="test_user_delete",
                          password="test_password_delete")

        response = self.client.post(reverse("users_delete",
                                            kwargs={"pk": user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects
                         .filter(username="test_user_delete").exists())
