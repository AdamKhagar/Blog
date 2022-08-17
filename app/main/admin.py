from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from main.models import (
    Category,
    Tag,
    Post
)
from config.admin import register


@register(User)
class MyUserAdmin(UserAdmin):...

class PostInline(TabularInline):
    model = Post
    extra = 0
    readonly_fields = ('tags', 'author', 'created_at', 'last_changed')

    def has_add_permission(self, request, obj) -> bool:
        return True

    def has_change_permission(self, request, obj: Post) -> bool:
        return False

    def has_delete_permission(self, request, obj: Post) -> bool:
        return request.user.is_staff


@register(Category)
class CategoryAdmin(ModelAdmin):
    inlines = (PostInline,)


@register(Tag)
class TagAdmin(ModelAdmin):
    readonly_fields = ('posts',)


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = (
        'title',
        'category',
        'author',
        'created_at',
        'last_changed'
    )
    filter_horizontal = ('tags',)
    fields = (
        'title',
        'slug',
        'author',
        'created_at',
        'last_changed',
        'category',
        'tags',
        'content'
    )
    readonly_fields = (
        'created_at',
        'last_changed',
        'author'
    )