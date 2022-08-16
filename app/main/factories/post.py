from factory.django import DjangoModelFactory
from factory import (
    Sequence,
    LazyAttribute,
    SubFactory,
    post_generation,
    Faker
)
from django.utils.text import slugify

from main.models.models import Post
from main.factories import CategoryFactory, UserFactory

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = Sequence(lambda x: f"Post #{x}")
    slug = LazyAttribute(lambda x: slugify(x.title))
    category = SubFactory(CategoryFactory)
    author = SubFactory(UserFactory)
    content = "content"

    @post_generation
    def tags(self, create, extracted, **kwargs):
        return