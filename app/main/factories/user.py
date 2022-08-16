from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from factory import (
    Sequence,
    PostGenerationMethodCall,
    Faker
)



class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = Sequence(lambda n: f"user {n}")
    password = PostGenerationMethodCall("set_password", "qwerty123")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

