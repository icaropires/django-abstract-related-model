Django Abstract Related Model
=============================

|Build Status|
==============

In django a related model can't be abstract because of db issues. This module offers a workaround, pratically it doesn't declare the abstract, just avoid it of being created on database, but allow the children. Database creation is needed so you can create relationships.

Installing
----------

.. code:: bash

    $ pip3 install django-abstract-related-model

and add `abstract_related_model` to INSTALLED_APPS.

Using
-----

.. code:: python

    from abstract_related_model.models import AbstractRelatedModel

    class ExampleAbstractRelatedModel(AbstractRelatedModel):
        pass


Running tests
-------------

Go into example folder

.. code:: bash

    $ cd example

and run them

.. code:: bash

    $ ./manage.py test

Troubleshooting
---------------

Check the example folder if you have any doubts. Or you can create an
issue.


.. |Build Status| image:: https://travis-ci.org/icaropires/django-abstract-related-model.svg?branch=master
