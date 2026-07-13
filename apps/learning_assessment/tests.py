from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_renders_brand_assets(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "cThink_logo.svg")
        self.assertContains(response, "hr_hero.JPG")
