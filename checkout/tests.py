from django.test import TestCase
from .models import Order, OrderLineItem


 # ----- VIEWS ----- #
# class Test_Checkout_Views(TestCase):
#     def test_get_checkout_page_as_unathenticated(self):
#         page = self.client.get("/checkout/")
#         self.assertEqual(page.status_code, 302)
#         redirect = self.client.get("/login/")
#         self.assertEqual(redirect.status_code, 404)


 # ----- MODELS ----- #

# class Test_Checkout_Models(TestCase):
#     def test_place_order(self):
#         order = Order(full_name='Test User', phone_number="1234567",
#                       country='Ireland', postcode='12345')
#         order.save()
#         self.assertEqual(order.full_name, "Test User")
#         self.assertEqual(order.phone_number, "1234567")
#         self.assertEqual(order.country, 'Ireland')
#         self.assertEqual(order.postcode, '12345')
#         self.assertFalse(order.county)
#         self.assertFalse(order.town_or_city)
#         self.assertFalse(order.street_address_1)
#         self.assertFalse(order.street_address_2)

#     def test_place_order_products(self):
#         order_line_item = OrderLineItem()
#         self.assertFalse(order_line_item.quantity)