from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class HomepageTestCase(TestCase):
    """Tests for the homepage view."""

    def setUp(self):
        self.client = Client()
        self.url = reverse('homepage')

    def test_home_template_used(self):
        response = self.client.get(self.url)
        self.assertIn('public/home.html', response.template_name)

    def test_anonymous_can_access(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_email_address_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('emma_email', response.context)
        self.assertEqual(
            settings.EMMA_EMAIL_ADDRESS,
            response.context['emma_email']
        )
