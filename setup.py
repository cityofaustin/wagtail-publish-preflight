from setuptools import setup, find_packages
from os import path
from publish_preflight import __version__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name='wagtail-publish-preflight',
    version=__version__,

    packages=find_packages(),
    include_package_data=True,

    description='Provides validation for publishing a page witout blocking draft saves',
    long_description=long_description,

    url='https://github.com/cityofaustin/wagtail-publish-preflight',

    author='Eric Sherman',
    author_email='ericandrewsherman@gmail.com',

    license='BSD-3-Clause',

    install_requires=[
        'wagtail>=1.11',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 1',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
