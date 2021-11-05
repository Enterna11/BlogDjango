from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_editable = ('is_published',)


admin.site.register(News, NewsAdmin)
