from django.test import TestCase
from .models import ExampleAbstractRelatedModel, ConcreteModel


class TestRelatedAbstractModel(TestCase):
    # pylint: disable=no-self-use

    def test_instatiate_abstract_model(self):
        expected_message = ("Can't save 'RelatedAbstractModel'"
                            " because it's abstract")
        with self.assertRaisesMessage(Exception, expected_message):
            ExampleAbstractRelatedModel.objects.create()

    def test_instatiate_concrete_model(self):
        ConcreteModel.objects.create()

    def test_create_relationship(self):
        first = ConcreteModel.objects.create()
        first.concrete_model = ConcreteModel.objects.create()
