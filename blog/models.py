from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Post(models.Model):
    image = models.ImageField(upload_to='blog/img/', default='blog/img/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tage
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-published_date"]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
       return "%s %s" % (self.title, self.id)


    def increment_counted_views(self):
        self.counted_views += 1
        self.save()



