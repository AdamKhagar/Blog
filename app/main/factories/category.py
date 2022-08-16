from factory.django import DjangoModelFactory
from factory import LazyAttribute, Sequence
from django.utils.text import slugify

from main.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = Sequence(lambda x: f"Category #{x}")
    slug = LazyAttribute(lambda x: slugify(x.name))


