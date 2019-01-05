from django.contrib import admin
from .models import Article


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "date", "author"]
#   list_display_links = ["updated"]
    list_filter = ["updated", "date"]
    search_fields = ["title", "body"]
    class Meta:
        model = Article



admin.site.register(Article, ArticleModelAdmin)


admin.site.site_header = 'Unit Zakat Unisel'
#admin.site.index_title = 'BUTIRAN PEMOHON'

#title
#index_title