from django.test import TestCase
from django.shortcuts import reverse

from users.models import User
from tasks.models import Task
from labels.models import Label


class LabelTest(TestCase):
    fixtures = ["sample.json"]

    def setUp(self):
        self.client.login(username="test_user",
                          password="test_password")
        self.user = User.objects.get(username="test_user")
        self.label = Label.objects.get(name="test_label")
        self.task = Task.objects.get(name="test_task")

    def test_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse("labels"))
        self.assertEqual(response.status_code, 302)

    def test_LabelsView(self):
        response = self.client.get(reverse("labels"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ID", response.content)
        self.assertIn(b"test_label", response.content)

    def test_LabelCreateView(self):
        self.client.post(reverse("labels_create"),
                         data={"name": "test_label_create"})

        new_label = Label.objects.filter(name="test_label_create")
        self.assertTrue(new_label.exists())

        response = self.client.get(reverse("labels_create"))
        self.assertEqual(response.status_code, 200)

    def test_LabelUpdateView(self):
        response = self.client.get(reverse("labels_update",
                                           kwargs={"pk": self.label.id}))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test_label", response.content)

        response = self.client.post(
            reverse("labels_update",
                    kwargs={"pk": self.label.id}),
            data={
                "name": "test_label_updated",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(Label.objects.filter(name="test_label").exists())
        self.assertTrue(
            Label.objects.filter(name="test_label_updated").exists())

    def test_LabelDeleteView(self):
        # when task exists
        response = self.client.post(reverse("labels_delete",
                                            kwargs={"pk": self.label.id}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name="test_label").exists())

        # when task removed
        self.label.task_set.all().delete()
        self.client.post(reverse("labels_delete",
                                 kwargs={"pk": self.label.id}))
        self.assertFalse(Label.objects.filter(name="test_label").exists())
