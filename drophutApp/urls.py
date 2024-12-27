from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'drophutApp.views.custom_404'

urlpatterns = [
  path('', views.index, name='index'),
  path('product/<int:product_id>/', views.product_details, name='product_details'),
  path('about', views.about, name='about'),
  path('blog', views.blog, name='blog'),
  path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
  path('faq', views.faq, name='faq'),
  path('privacy-policy', views.privacy_policy, name='privacy_policy'),
  path('contact', views.contact, name='contact'),
  path('cart/', views.cart, name='cart'),
  path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
  path('tracking', views.tracking, name='tracking'),
  path('wishlist/', views.wishlist, name='wishlist'),
]