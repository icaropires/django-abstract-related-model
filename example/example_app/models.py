from django.db import models
from abstract_related_model.models import AbstractRelatedModel


class ExampleAbstractRelatedModel(AbstractRelatedModel):

    concrete_model = models.ForeignKey(
        'ConcreteModel',
        on_delete=models.CASCADE
    )


class ConcreteModel(ExampleAbstractRelatedModel):
    pass
