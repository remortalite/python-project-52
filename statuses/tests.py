from django.test import TestCase
from django.urls import reverse
import logging

from statuses.models import Status

logger = logging.getLogger(__name__)


class StatusViewTest(TestCase):
    fixtures = ["sample.json"]

    def setUp(self):
        self.client.login(username="test_user",
                          password="test_password")
        self.status = Status.objects.get(name="test_status")

    def test_read_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("statuses"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_read_authorized(self):
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test_status", response.content)

    def test_create(self):
        self.client.post(reverse("statuses_create"),
                         data={"name": "new_test_status"})
        self.client.get(reverse("statuses"))
        self.assertTrue(Status.objects.filter(name="new_test_status").exists())

    def test_update(self):
        response = self.client.get(reverse("statuses_update",
                                           kwargs={"pk": self.status.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test_status", response.content)

        self.client.post(reverse("statuses_update",
                                 kwargs={"pk": self.status.id}),
                         data={"name": "test_status_updated"})

        self.assertTrue(Status.objects.filter(name="test_status_updated")
                        .exists())
        self.assertFalse(Status.objects.filter(name="test_status").exists())

    def test_delete(self):
        self.client.post(reverse("statuses_delete",
                                 kwargs={"pk": self.status.id}))
        self.assertFalse(Status.objects.filter(name="test_status").exists())
