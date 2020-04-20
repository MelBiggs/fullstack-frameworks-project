from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponsePermanentRedirect
from django.forms import modelform_factory
from products.forms import ReviewForm
from products.models import Product, Review, Tag


# ----- FORMS ----- #
class Review_Form(TestCase):
    def test_valid(self):
        form_data={"title":"My review", "body":"Review content",
                   "score": "3"}
        form= ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid(self):
        form_data={"title":"", "body":"", "score": ""}
        form= ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["title"], [u"This field is required."])
        self.assertEqual(
            form.errors["body"], [u"This field is required."])
        self.assertEqual(
            form.errors["score"], [u"This field is required."])


# # ----- MODELS ----- #
class Product_Model_Test(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product",
                                              price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")
        self.product2 = Product.objects.create(name="Test Product2",
                                               price="30",
                                               category="B",
                                               description="Test Description2",
                                               product_type="C",
                                               image="test_img2.jpeg")

    def test_get_product(self):
        product = Product.objects.filter(name="Test Product").first()
        self.assertEqual(product, self.product)

    def test_get_product_filter_count(self):
        count = Product.objects.filter(name="Test Product").count()
        self.assertEqual(count, 1)

    def test_get_product_count(self):
        count = Product.objects.all().count()
        self.assertEqual(count, 2)

    def test_to_string(self):
        product = Product.objects.filter(name="Test Product").first()
        self.assertEqual(product.__str__(), "Test Product")

    def test_category(self):
        product = Product.objects.filter(name="Test Product").first()
        self.assertEqual(product.get_category_display(), "Face")

    def test_type(self):
        product = Product.objects.filter(name="Test Product").first()
        self.assertEqual(product.get_product_type_display(), "Moisturiser")


 # ----- VIEWS ----- #

class Product_View_Test(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product",
                                              price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")
        self.product2 = Product.objects.create(name="Test Product2",
                                               price="30",
                                               category="B",
                                               description="Test Description2",
                                               product_type="C",
                                               image="test_img2.jpeg")
        self.product3 = Product.objects.create(name="Test Product3",
                                               price="40",
                                               category="B",
                                               description="Test Description3",
                                               product_type="E",
                                               image="test_img3.jpeg")
        Tag.objects.create(product=self.product2, value="EC")
        Tag.objects.create(product=self.product2, value="AC")
        Tag.objects.create(product=self.product, value="RO")
        Tag.objects.create(product=self.product, value="AC")
        Tag.objects.create(product=self.product3, value="AC")
        Tag.objects.create(product=self.product3, value="RO")
        Tag.objects.create(product=self.product3, value="SU")
        self.user=User.objects.create_user(username="TestUser",
                                           email="testemail@gmail.com",
                                           password="Password")


    def test_products_view_all(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 3)
        self.assertTemplateUsed(page, "products.html")

    def test_body_products_view_all(self):
        page = self.client.get("/products/body")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 2)
        self.assertTemplateUsed(page, "products.html")

    def test_face_products_view_all(self):
        page = self.client.get("/products/face")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 1)
        self.assertTemplateUsed(page, "products.html")

    def test_products_view_tagged(self):
        page = self.client.get("/products/?RO=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 2)
        self.assertTemplateUsed(page, "products.html")

    def test_products_view_tagged_multiple(self):
        page = self.client.get("/products/?RO=on&AC=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 3)
        self.assertTemplateUsed(page, "products.html")

    def test_products_view_tagged_no_results(self):
        page = self.client.get("/products/?S=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 0)
        self.assertTemplateUsed(page, "products.html")

    def test_body_products_view_tagged(self):
        page = self.client.get("/products/body/?RO=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 1)
        self.assertTemplateUsed(page, "products.html")

    def test_body_products_view_tagged_no_results(self):
        page = self.client.get("/products/body/?S=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 0)
        self.assertTemplateUsed(page, "products.html")

    def test_face_products_view_tagged(self):
        page = self.client.get("/products/face/?AC=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 1)
        self.assertTemplateUsed(page, "products.html")

    def test_face_products_view_tagged_no_results(self):
        page = self.client.get("/products/face/?SU=on")
        self.assertEqual(page.status_code, 200)
        products = page.context["products"]
        self.assertEqual(len(products), 0)
        self.assertTemplateUsed(page, "products.html")

    def test_review_not_logged_in(self):
        product_id = self.product.pk
        page = self.client.post(
            "/products/"+str(product_id),
            {"title": "Test Review",
                "body": "Test description",
                "score": "3"})
        reviews = Review.objects.all().count()
        self.assertEqual(reviews, 0)
        self.assertEquals(page.status_code, 301)
