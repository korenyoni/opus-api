#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "click>=6.7",
    "beautifulsoup4>=4.6.0",
    "requests>=2.19.1",
    "diskcache>=3.0.6",
    "selenium>=3.13.0",
    "cryptography>=2.3",
]

setup_requirements = [
    # TODO(yonkornilov): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='opus_api',
    version='0.6.2',
    description="OPUS (opus.nlpl.eu) Python API",
    long_description="OPUS (opus.nlpl.eu) Python3 API and CLI.\
    Read the `documentation <http://opus-api.readthedocs.io>`__.",
    author="Yonathan Koren",
    author_email='yonkornilov@live.com',
    url='https://github.com/yonkornilov/opus-api',
    packages=find_packages(include=['opus_api']),
    entry_points={
        'console_scripts': [
            'opus_api=opus_api.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=['opus_api', 'api', 'parallel', 'corpora', 'mmt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
