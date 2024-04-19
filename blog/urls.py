from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # path('<int:pid>/', blog_test, name='test'),   # test
    path('test', blog_test, name='test'),   # test
    path('', blog_view, name='index'),
    path('<int:pid>/', blog_single, name='single'),
]
