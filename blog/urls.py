from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, get_posts_by_tag, delete_comment

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^tag/(?P<tag>.*)/$', get_posts_by_tag, name='get_posts_by_tag'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/review/(?P<rk>\d+)$', delete_comment, name='delete_comment'),
    ]
