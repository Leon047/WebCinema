from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MovieDescription


@admin.register(MovieDescription)
class MovieDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_date', 'image_show')
    list_display_links = ('title', 'image_show')
    list_filter = ('title',)

    def image_show(self, obj):
        if obj.poster:
            return mark_safe("<img src='/static/images{}' width='150px'/>" .format(obj.poster.url))
        return None
    image_show.__name__='Picture'
