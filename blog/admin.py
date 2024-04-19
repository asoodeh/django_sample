from django.contrib import admin
from blog.models import Post, Category
from blog.models import Post, Category
# Register your models here.


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    fields = ('title', 'image', 'author', 'content', 'category', 'counted_views', 'status', 'published_date')    # show fields
    exclude = [""]    # != field
    list_display = ('id', 'title', 'image', 'author', 'counted_views', 'status', 'published_date', 'created_date', 'updated_date')    # show fields in table page
    list_filter = ('counted_views', 'author', 'status', 'category', 'published_date')
    search_fields = ['title', 'author', 'content', ]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
