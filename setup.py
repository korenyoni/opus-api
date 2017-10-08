#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as req_file:
    required = req_file.read().splitlines()

requirements = required

setup_requirements = [
    # TODO(yonkornilov): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='opus_api',
    version='0.1.7',
    description="OPUS (opus.lingfil.uu.se) Python API",
    long_description=readme + '\n\n' + history,
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
    keywords='opus_api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
