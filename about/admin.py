from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Post)
#admin.site.register(About)