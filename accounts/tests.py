from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import Favourite
from products.models import Product

# ----- FORMS ----- #

class Test_User_Login_Form(TestCase):
    def test_log_in_valid(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": "Password"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])


class Test_User_Registration_Form(TestCase):
    def test_register_form_valid(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "testemail@gmail.com",
                "password1": "TestPassword", "password2": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_passwords_do_not_match(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "testemail@gmail.com",
                "password1": "TestPassword", "password2": "TestPassword123"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords must match!"])

# ----- VIEWS----- #

class Accounts_View_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="TestUser",
                                             email="testemail@gmail.com",
                                             password="Password")
        self.product = Product.objects.create(name="Test Product",
                                              price="20",
                                              category="F",
                                              description="Test Description",
                                              product_type="M",
                                              image="test_img.jpeg")

    def test_login_view(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_logout_view(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)

    def test_register_view(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_profile_view(self):
        self.client.login(username="TestUser", password="Password")
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)

    # def test_favourite(self):
    #     self.client.login(username="TestUser", password="Password")
    #     page = self.client.get("/accounts/favourite/"+ str(self.product.pk))
    #     favourites = Favourite.objects.all()
    #     self.assertEqual(favourites.count(), 1)
    #     # Unfavouriting
    #     page = self.client.get("/accounts/favourite/"+ str(self.product.pk))
    #     favourites = Favourite.objects.all()
    #     self.assertEqual(favourites.count(), 0)
