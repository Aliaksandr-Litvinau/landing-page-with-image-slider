from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin

from nasa.models import Images, SliderImages


class ChapterTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SliderImages
    fields = ['image']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


@admin.register(Images)
class SortableBookAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ChapterTabularInline]


admin.site.site_title = 'Nasa_Project'
admin.site.site_header = 'Nasa_Project'
