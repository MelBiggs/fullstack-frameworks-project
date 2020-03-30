from django.conf.urls import url
from .views import (all_products, face_products, body_products, product_detail,
                    cleanser_products, exfoliator_products, serum_products,
                    moisturiser_products, sunscreen_products, toner_products,
                    masks_products, eye_products, chemical_products)

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^face', face_products, name='face_products'),
    url(r'^body', body_products, name='body_products'),
    url(r'^cleanser', cleanser_products, name='cleanser_products'),
    url(r'^exfoliator', exfoliator_products, name='exfoliator_products'),
    url(r'^serum', serum_products, name='serum_products'),
    url(r'^moisturiser', moisturiser_products, name='moisturiser_products'),
    url(r'^sun', sunscreen_products, name='sunscreen_products'),
    url(r'^toners', toner_products, name='toner_products'),
    url(r'^masks', masks_products, name='masks_products'),
    url(r'^eyes', eye_products, name='eye_products'),
    url(r'^chemical', chemical_products, name='chemical_products'),
]
