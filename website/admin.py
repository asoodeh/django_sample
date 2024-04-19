from django.contrib import admin


from website.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    fields = ('name', 'email', 'subject', 'message',  'created_date', 'updated_date')    # show fields
    exclude = [""]    # != field
    list_display = ('name', 'email', 'subject', 'created_date', 'updated_date')    # show fields in table page
    list_filter = ('subject', 'email', 'created_date')
    search_fields = ['name', 'email', 'subject', 'message']

