from django.contrib import admin
from .models import Notice


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "updated", "date"]
    list_display_links = ["updated"]
    list_filter = ["updated", "date"]
    search_fields = ["title"]
    class Meta:
        model = Notice




admin.site.register(Notice, NoticeModelAdmin)