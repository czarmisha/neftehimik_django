from django.urls import path
from main_app.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('products/', products_page, name='products'),
    path('products/detail/<int:pk>', product_detail, name='product_detail'),
    path('about_us/', about_page, name='about_us'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/detail/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('contacts/', contacts_page, name='contacts'),
    path('send_massage_to_manager/<int:pk>/', send_message, name='send_message'),
    path('contact_message/', contact_message, name='contact_message'),
    path('search/', search, name='search'),
]