from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Post, Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = (CommentAdminInline, )
    list_display = ('title', 'created_date')
    list_filter = (
        ('published_date', DateFieldListFilter),
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'approved')
    list_filter = (
        ('published_date', DateFieldListFilter),
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
