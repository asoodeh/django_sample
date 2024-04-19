from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_test(request):
    post = Post.objects.all()
    context = {'Firstname': 'ali', 'Lastname': 'asoodeh', 'Email': 'asoodeh.ali@gmail.com', 'post': post}
    return render(request, 'blog/test.html', context)

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
     posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
     post = get_object_or_404(posts, pk=pid)
     previous_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1, published_date__lt=post.published_date).order_by('published_date')
     previous_post = previous_posts.last()
     next_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1, published_date__gt=post.published_date).order_by('published_date')
     next_post = next_posts.first()


     post.increment_counted_views()
     context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
     return render(request, 'blog/blog-single.html', context)


