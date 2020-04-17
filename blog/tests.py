from django.test import TestCase
from blog.forms import BlogPostForm, CommentForm
from django.contrib.auth.models import User
from blog.models import Post, Comment


# ----- FORMS ----- #
class Blogpost_Form(TestCase):
    def test_valid(self):
        form_data={"title":"My blog", "content":"Blog content", "image": "test_img.jpeg",
        "tag":"Meta", "published_date":"2020-06-15 00:00:00", "writer":"User"}
        form= BlogPostForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid(self):
        form_data={"title":"", "content":"", "image": "",
        "tag":"", "published_date":"", "writer":""}
        form= BlogPostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["title"], [u"This field is required."])
        self.assertEqual(
            form.errors["content"], [u"This field is required."])
        self.assertEqual(
            form.errors["writer"], [u"This field is required."])


class Comment_Form(TestCase):
    def test_valid(self):
        form_data={"body":"Comment content"}
        form= CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid(self):
        form_data={"body":""}
        form= CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["body"], [u"This field is required."])


# # ----- MODELS ----- #

class Blog_Model_Test(TestCase):   
    def setUp(self):
        self.post = Post.objects.create(title="Test Blog", writer="User",
        content="Blog content", created_date="2020-04-15 00:00:00", published_date="2020-04-15",
        views="2", tag="test", image="test_img.jpeg")
        self.post2 = Post.objects.create(title="Test Blog2", writer="User2",
        content="Blog content2", created_date="2020-05-15 00:00:00", published_date="2020-05-15",
        views="3", tag="test", image="test_img2.jpeg")
        self.post3 = Post.objects.create(title="Test Blog3", writer="User",
        content="Blog content3", created_date="2020-06-15 00:00:00", published_date="2020-06-15",
        views="4", tag="test2", image="test_img3.jpeg")

    def test_get_post(self):
        post = Post.objects.filter(title="Test Blog").first()
        self.assertEqual(post, self.post)
    
    def test_get_post_count(self):
        count = Post.objects.all().count()
        self.assertEqual(count, 3)


 # ----- VIEWS ----- #

class Post_View_Test(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Blog", writer="User",
        content="Blog content", created_date="2020-04-15 00:00:00", published_date="2020-04-15",
        views="2", tag="test", image="test_img.jpeg")
        self.post2 = Post.objects.create(title="Test Blog2", writer="User2",
        content="Blog content2", created_date="2020-05-15 00:00:00", published_date="2020-05-15",
        views="3", tag="test", image="test_img2.jpeg")
        self.post3 = Post.objects.create(title="Test Blog3", writer="User",
        content="Blog content3", created_date="2020-06-15 00:00:00", published_date="2020-06-15",
        views="4", tag="test2", image="test_img3.jpeg")
        self.user = User.objects.create(username="TestUser",
        email="testemail@gmail.com")
        self.user.set_password("Password")
        self.user.save()

    def test_posts_view_all(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        posts = page.context["posts"]
        self.assertEqual(len(posts), 3)
        self.assertTemplateUsed(page, "blogposts.html")

    def test_post_view_tagged(self):
        page = self.client.get("/blog/tag/test/")
        self.assertEqual(page.status_code, 200)
        posts = page.context["posts"]
        self.assertEqual(len(posts), 2)
        self.assertTemplateUsed(page, "blogposts.html")

    def test_posts_view_tagged_no_results(self):
        page = self.client.get("/blog/tag/test3/")
        self.assertEqual(page.status_code, 200)
        posts = page.context["posts"]
        self.assertEqual(len(posts), 0)
        self.assertTemplateUsed(page, "blogposts.html")

    def test_comment_not_logged_in(self):
        post_id = self.post.pk
        page = self.client.post(
            "/blog/"+str(post_id),
            {"body": "Test description"})
        comments = Comment.objects.all().count()
        self.assertEqual(comments, 0)
        self.assertEquals(page.status_code, 301)
