from django.test import TestCase
from products.models import Product
from blog.models import Post


 # ----- VIEWS ----- #

# ----- PRODUCT SEARCH ----- #
class Search_Product_Test(TestCase):   
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price="20",
        category="F", description="Test Description", product_type="M",
        image="test_img.jpeg")
        self.product2 = Product.objects.create(name="Other Product", price="30",
        category="B", description="Test Description2", product_type="C",
        image="test_img2.jpeg")

    def test_search_products(self):
        page = self.client.get("/search/?q=test%20product")
        products = page.context["products"]
        self.assertEqual(len(products), 1)
        self.assertTemplateUsed(page, "products.html")

    def test_search_products_multiple(self):
        page = self.client.get("/search/?q=product")
        products = page.context["products"]
        self.assertEqual(len(products), 2)
        self.assertTemplateUsed(page, "products.html")    

    def test_search_products_none(self):
        page = self.client.get("/search/?q=random")
        products = page.context["products"]
        self.assertEqual(len(products), 0)
        self.assertTemplateUsed(page, "products.html")  
    

# ----- BLOG SEARCH ----- #

# class Search_Blog_Test(TestCase):   
#     def setUp(self):
#         self.post = Post.objects.create(title="Test Blog", writer="User",
#         content="Blog content", created_date="2020-04-15 00:00:00", published_date="2020-04-15",
#         views="2", tag="test", image="test_img.jpeg")
#         self.post2 = Post.objects.create(title="Other Blog", writer="User",
#         content="Blog content", created_date="2020-04-15 00:00:00", published_date="2020-04-15",
#         views="2", tag="test", image="test_img.jpeg")

#     def test_search_posts(self):
#         page = self.client.get("/search/blog/?q=blog%20test")
#         posts = page.context["posts"]
#         self.assertEqual(len(posts), 1)
#         self.assertTemplateUsed(page, "blogposts.html")

#     def test_search_posts_multiple(self):
#         page = self.client.get("/search/blog/?q=other")
#         posts = page.context["posts"]
#         self.assertEqual(len(posts), 2)
#         self.assertTemplateUsed(page, "blogposts.html")    

#     def test_search_posts_none(self):
#         page = self.client.get("/search/blog/?q=random")
#         posts = page.context["posts"]
#         self.assertEqual(len(posts), 0)
#         self.assertTemplateUsed(page, "blogposts.html")  
