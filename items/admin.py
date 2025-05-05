from django.contrib import admin
from .models import Item, Comment


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('item', 'text', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('created_at',)