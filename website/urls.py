
from django.urls import path
# from website.views import http_test,json_test
from website.views import *

app_name = 'website'

urlpatterns = [
    # path('http_test',http_test),
    # path('json_test',json_test),
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('blog-home', contact_view, name='blog-home'),
    path('blog-single', contact_view, name='blog-single'),
     path('elements', contact_view, name='elements'),
]
