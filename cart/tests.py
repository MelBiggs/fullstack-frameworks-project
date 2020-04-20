from django.test import TestCase
from products.models import Product


# # ----- VIEWS ----- #
class Cart_View_Test(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")

    def test_add_to_cart(self):
        product_id = self.product.pk
        request = self.client.post("/cart/add/"+str(product_id),
                                   data={"quantity":"2"})
        self.assertEqual(request.status_code, 302)
        session = self.client.session
        self.assertEqual(session["cart"][str(product_id)], 2)

    def test_adjust_cart(self):
        product_id = self.product.pk
        self.client.post("/cart/add/"+str(product_id),
                         data={"quantity":"2"})
        request = self.client.post("/cart/adjust/"+str(product_id),
                                   data={"quantity":"4"})
        self.assertEqual(request.status_code, 302)
        session = self.client.session
        self.assertEqual(session["cart"][str(product_id)], 4)

    def test_adjust_cart_to_zero(self):
        product_id = self.product.pk
        self.client.post("/cart/add/"+str(product_id), data={"quantity":"2"})
        request = self.client.post("/cart/adjust/"+str(product_id),
                                   data={"quantity":"0"})
        self.assertEqual(request.status_code, 302)
        session = self.client.session
        self.assertFalse(str(product_id) in session["cart"])

    def test_remove_from_cart(self):
        product_id = self.product.pk
        self.client.post("/cart/add/"+str(product_id),
                         data={"quantity":"2"})
        request = self.client.get("/cart/remove/"+str(product_id))
        self.assertEqual(request.status_code, 302)
        session = self.client.session
        self.assertEqual(session["cart"][str(product_id)], 1)

    def test_remove_from_cart_to_zero(self):
        product_id = self.product.pk
        self.client.post("/cart/add/"+str(product_id),
                         data={"quantity":"1"})
        request = self.client.get("/cart/remove/"+str(product_id))
        self.assertEqual(request.status_code, 302)
        session = self.client.session
        self.assertFalse(str(product_id) in session["cart"])
