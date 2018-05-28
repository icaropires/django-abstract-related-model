import os
from setuptools import setup

install_requires = [
    'django'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django_abstract_related_model',
    version='0.1.1',
    description="Workaround for related abstract models issue.",
    url='https://github.com/icaropires/django-related-abstract-model',
    author='Ícaro Pires',
    author_email='icaropsa@gmail.com',
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    packages=['abstract_related_model'],
    install_requires=install_requires,
    long_description=read('README.rst'),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
