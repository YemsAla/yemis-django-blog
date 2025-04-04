from django.contrib import admin

# Register your models here.
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'content','updated_on',)
    search_fields = ['title', 'content',]
    list_filter = ('title', 'updated_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.

admin.site.register(About)

