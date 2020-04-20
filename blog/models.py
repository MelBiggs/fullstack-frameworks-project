from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, default="Melissa Biggs")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                      default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A comment 
    """
    body = models.TextField()
    approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    post = models.ForeignKey(Post,
                             related_name="comments", on_delete=models.CASCADE,
                             related_query_name="comment", null=True)
    user = models.ForeignKey(User, related_name="comments",
                             on_delete=models.CASCADE,
                             related_query_name="comment", null=True)

    class Meta:
        ordering = ['-published_date']
