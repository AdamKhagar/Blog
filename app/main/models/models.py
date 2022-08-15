from django.utils.translation import gettext_lazy as _
from django.db import models 
from django.contrib.auth.models import User

from main.models.common import NameSlugBaseModel



class Category(NameSlugBaseModel):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Tag(NameSlugBaseModel):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.CharField(_("Slug"), max_length=255, unique=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        related_name="posts",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        related_name="posts",
        on_delete=models.CASCADE,
        editable=False
    )
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return f"{self.category if self.category else '#'}:{self.title}"