from factory.django import DjangoModelFactory
from factory import Sequence, LazyAttribute
from django.utils.text import slugify

from main.models import Tag


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = Sequence(lambda x: f"Tag #{x}")
    slug = LazyAttribute(lambda x: slugify(x.name))
