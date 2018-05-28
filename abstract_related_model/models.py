from django.db import models


class AbstractRelatedModel(models.Model):

    def save(self, *args, **kwargs):
        # pylint: disable=arguments-differ, unused-argument
        if AbstractRelatedModel in self.__class__.__bases__:
            raise Exception(
                "Can't save 'RelatedAbstractModel' because it's abstract"
            )
