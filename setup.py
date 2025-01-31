#!/usr/bin/env python

import os
import sys

from setuptools import setup

_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))
try:
    import markdown_deux
finally:
    del sys.path[0]
README = open(os.path.join(_top_dir, 'README.md')).read()

setup(
    name='django-markdown-deux',
    version=markdown_deux.__version__,
    description="a Django app that provides template tags for using Markdown (using the python-markdown2 processor)",
    long_description=README,
    classifiers=[c.strip() for c in """
        Development Status :: 5 - Production/Stable
        Environment :: Web Environment
        Framework :: Django
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2
        Topic :: Internet :: WWW/HTTP
        """.split('\n') if c.strip()],
    keywords='django markdown markdown2 text markup html',
    author='Trent Mick',
    author_email='trentm@gmail.com',
    maintainer='Trent Mick',
    maintainer_email='trentm@gmail.com',
    url='http://github.com/trentm/django-markdown-deux',
    license='MIT',
    install_requires=['markdown2'],
    packages=["markdown_deux"],
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
)
