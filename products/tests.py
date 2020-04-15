from django.test import TestCase
from products.forms import ReviewForm


# ----- FORMS ----- #
class ReviewForm(TestCase):
    def test_users_can_create_a_new_review(self):
        form = ReviewForm(
            {"title": "My New Test Review",
                "body": "My test description of a fake Bug!"
                "score": "2"})
        self.assertTrue(form.is_valid())
    
    def test_correct_error_message(self):
        form = ReviewForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["title"], [u"This field is required."])


# ----- MODELS ----- #
class ProductEntryTest(TestCase):
    def test_get_absolute_url(self):
        pk = 99
        name = "Test Product"
        expected_result = '/products/' + str(pk) + '/'

        product = Product(pk=pk, name=name)
        result = Product.get_absolute_url(product)

        self.assertEqual(result, expected_result)
