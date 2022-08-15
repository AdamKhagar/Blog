from django.db import models
from django.utils.translation import gettext_lazy as _


class NameSlugBaseModel(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name