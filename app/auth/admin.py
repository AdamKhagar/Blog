from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from config.admin import register


@register(User)
class MyUserAdmin(UserAdmin):...