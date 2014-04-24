#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='osm_field',
    version='0.0.0',
    description='Django OpenStreetMap Field',
    long_description=readme + '\n\n' + history,
    author='Sinnwerkstatt Medienagentur GmbH',
    author_email='web@sinnwerkstatt.com',
    url='http://git.sinnwerkstatt.com/sinnwerkstatt/osm-field',
    packages=[
        'osm_field',
    ],
    package_dir={'osm_field': 'osm_field'},
    include_package_data=True,
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords='osm_field',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
