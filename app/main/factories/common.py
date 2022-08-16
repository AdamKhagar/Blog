from typing import List

from factory.django import DjangoModelFactory
from django.db.models import Model
from django.db.utils import IntegrityError


def create_unique_records(factory: DjangoModelFactory, size: int, **factory_kwargs) -> List[Model]:
    counter = 0
    model_list = []
    while counter < size:
        try:
            model = factory.create(**factory_kwargs)
        except IntegrityError:
            pass
        else:
            counter += 1
            model_list.append(model)

    return model_list 