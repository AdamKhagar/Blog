from django.contrib.admin import ModelAdmin
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


@register(Category)
class CategoryAdmin(ModelAdmin):...


@register(Tag)
class TagAdmin(ModelAdmin):...


@register(Post)
class PostAdmin(ModelAdmin):...