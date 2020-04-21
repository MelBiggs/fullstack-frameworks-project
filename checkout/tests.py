from django.test import TestCase
from products.models import Product
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Order, OrderLineItem
from .forms import MakePaymentForm, OrderForm
from datetime import date


# ----- FORMS ----- #

class Test_Order_Form(TestCase):
    def test_successful_order_entry(self):
        form = OrderForm({
            'full_name': 'Test User', 
            'phone_number': '12345678', 
            'country': 'Ireland',  
            'postcode': '12345', 
            'town_or_city': 'Dublin', 
            'street_address1': '12 Test Street',
            'street_address2': 'Test Avenue', 
            'county': 'Dublin',
            })
        self.assertTrue(form.is_valid())   

    def test_invalid(self):
        form_data={"full_name": "", "phone_number": "", "street_address1": "",
                   "street_address2": "", "town_or_city": "", "county": "",
                   "country": ""}
        form= OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["full_name"], [u"This field is required."])
        self.assertEqual(
            form.errors["street_address1"], [u"This field is required."])
        self.assertEqual(
            form.errors["phone_number"], [u"This field is required."])

    def test_successful_order_entry_with_blank_field(self):
        form = OrderForm({
            'full_name': 'Test User', 
            'phone_number': '12345678', 
            'country': 'Ireland',  
            'postcode': '', 
            'town_or_city': 'Dublin', 
            'street_address1': '12 Test Street',
            'street_address2': 'Test Avenue', 
            'county': 'Dublin',
            })
        self.assertTrue(form.is_valid())

    
class TestMakePaymentForm(TestCase):
    def test_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number': '', 'cvv': ''})
        self.assertFalse(form.is_valid())

# ----- VIEWS ----- #

class Test_Checkout_Views(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product",
                                              price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")
        self.user=User.objects.create_user(username="TestUser",
                                           email="testemail@gmail.com",
                                           password="Password")

    def test_checkout_card_accepted(self):
        self.client.login(username="TestUser", password="Password")
        s = self.client.session
        s.update({"cart": "1"})
        s.save
        order_data = {'full_name':'Test User', 'phone_number':'1234567',
                      'street_address1':'12 Test St',
                      'street_address2':'Test',
                      'town_or_city': 'Dublin',
                      'county': 'Co Dublin',
                      'country': 'Ireland',
                      'credit_card_number':'4242424242424242', 'cvv':'123',
                      'expiry_month':'6','expiry_year':'2020'}
        response = self.client.post('/checkout', order_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_checkout_card_declined(self):
        self.client.login(username="TestUser", password="Password")
        s = self.client.session
        s.update({"cart": "1"})
        s.save
        order_data = {'full_name':'Test User', 'phone_number':'1234567',
                      'street_address1':'12 Test St',
                      'street_address2':'Test',
                      'town_or_city': 'Dublin',
                      'county': 'Co Dublin',
                      'country': 'Ireland',
                      'credit_card_number':'4242424242424242', 'cvv':'123',
                      'expiry_month':'6','expiry_year':'2020',
                      'stripe_id': 'tok_chargeDeclined'}
        response = self.client.post('/checkout', order_data, follow=True)
        self.assertEqual(response.status_code, 200)

        for message in get_messages(response.wsgi_request):
            self.assertEqual('Your card was declined!', messages)

    def test_get_checkout_page_as_unauthenticated(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)


 # ----- MODELS ----- #

class Test_Checkout_Models(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product",
                                              price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")

    def test_place_order(self):
        order = Order(full_name='Test User', phone_number="1234567",
                      country='Ireland', postcode='12345',
                      town_or_city="Dublin",
                      street_address1="Test Street",
                      street_address2="Test Avenue",
                      county= "Dublin",
                      date= date.today())
        order.save()
        self.assertEqual(order.full_name, "Test User")
        self.assertEqual(order.phone_number, "1234567")
        self.assertEqual(order.country, 'Ireland')
        self.assertEqual(order.postcode, '12345')
        self.assertEqual(order.town_or_city, 'Dublin')
        self.assertEqual(order.street_address1, 'Test Street')
        self.assertEqual(order.street_address2, 'Test Avenue')
        self.assertEqual(order.county, 'Dublin')
        
        
    def test_place_order_products(self):
        order = Order(full_name='Test User', phone_number="1234567",
                      country='Ireland', postcode='12345',
                      date= date.today())
        order.save()
        order_line_item = OrderLineItem(order=order, product=self.product,
                                        quantity=3)
        order_line_item.save()
        self.assertEqual(order_line_item.quantity, 3)
        self.assertEqual(len(order.line_items.all()), 1)
        self.assertEquals(order.line_items.first(), order_line_item)
