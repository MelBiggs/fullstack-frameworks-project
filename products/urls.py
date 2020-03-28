from django.conf.urls import url
from .views import all_products, face_products, body_products, product_detail

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^face', face_products, name='face_products'),
    url(r'^body', body_products, name='body_products'),
]
