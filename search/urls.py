from django.conf.urls import url
from .views import do_search, do_blog_search

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^blogs', do_blog_search, name='blogsearch')
]
