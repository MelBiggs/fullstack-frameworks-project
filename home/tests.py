from django.test import TestCase


class Home_View_Test(TestCase):
    def test_index_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
