from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import EmailMessage

class EmailListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('email_list')

    def test_email_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/email_list.html')
