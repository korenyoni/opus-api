::

                /$$$$$$            /$$$$$$$  /$$   /$$  /$$$$$$
               /$$__  $$          | $$__  $$| $$  | $$ /$$__  $$
      /$$$$$$$| $$  \ $$  /$$$$$$ | $$  \ $$| $$  | $$| $$  \__/
     /$$_____/| $$  | $$ /$$__  $$| $$$$$$$/| $$  | $$|  $$$$$$
    | $$      | $$  | $$| $$  \__/| $$____/ | $$  | $$ \____  $$
    | $$      | $$  | $$| $$      | $$      | $$  | $$ /$$  \ $$
    |  $$$$$$$|  $$$$$$/| $$      | $$      |  $$$$$$/|  $$$$$$/
     \_______/ \______/ |__/      |__/       \______/  \______/

|pypi| |build| |Documentation Status| |Updates|

`OPUS <http://opus.nlpl.eu/>`__ (opus.nlpl.eu) Python API

-  Free software: MIT license
-  Documentation: https://opus-api.readthedocs.io.

Requirements
============

Download `PhantomJS`_ and make sure its in your PATH, eg:

.. _`PhantomJS`: http://phantomjs.org/download.html

::

    $ wget -qO- https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar xvj -C ~/.local/bin --strip 2 phantomjs-2.1.1-linux-x86_64/bin

Installation
============

Stable release
--------------

To install Opus API, run this command in your terminal:

::

    $ pip install opus_api

This is the preferred method to install Opus API, as it will always
install the most recent stable release.

If you don't have `pip <https://pip.pypa.io>`__ installed, this `Python
installation
guide <http://docs.python-guide.org/en/latest/starting/installation/>`__
can guide you through the process.

From sources
------------

The sources for Opus API can be downloaded from the `Github
repo <https://github.com/yonkornilov/opus_api>`__.

You can either clone the public repository:

::

    $ git clone git://github.com/yonkornilov/opus_api

Or download the
`tarball <https://github.com/yonkornilov/opus_api/tarball/master>`__:

::

    $ curl  -OL https://github.com/yonkornilov/opus_api/tarball/master

Once you have a copy of the source, you can install it with:

::

    $ make install

Usage
=====

Find your languages:

::

    $ opus_api langs

    [
    ...
      {
        "description": "en (English)", 
        "id": 69, 
        "name": "en"
      },
      ...
      {
        "description": "ru (Russian)", 
        "id": 198, 
        "name": "ru"
      }...
    ...
    ]

Find corpora:

::

    $ opus_api get en ru --maximum 300 --minimum 3

    {
      "corpora": [
        {
          "id": 1, 
          "name": "OpenSubtitles2016", 
          "src_tokens": "157.5M", 
          "trg_tokens": "133.6M", 
          "url": "http://opus.nlpl.eu/download.php?f=OpenSubtitles2016%2Fen-ru.txt.zip"
        },
      ...
        {
          "id": 13, 
          "name": "KDE4", 
          "src_tokens": "1.8M", 
          "trg_tokens": "1.4M", 
          "url": "http://opus.nlpl.eu/download.php?f=KDE4%2Fen-ru.txt.zip"
        }
      ]
    }

TODO
====

1. Get: parallel corpora for formats other than MOSES and TMX
2. New feature: query available languages for corpora set

Credits
=======

This package's CLI is powered by
`click <https://github.com/pallets/click>`__.

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

.. |pypi| image:: https://img.shields.io/pypi/v/opus-api.svg
   :target: https://pypi.python.org/pypi/opus-api

.. |build| image:: https://img.shields.io/travis/yonkornilov/opus-api.svg
   :target: https://travis-ci.org/yonkornilov/opus-api

.. |Documentation Status| image:: https://img.shields.io/readthedocs/opus-api.svg
   :target: http://opus-api.readthedocs.io/en/latest/?badge=latest

.. |Updates| image:: https://pyup.io/repos/github/yonkornilov/opus-api/shield.svg
   :target: https://pyup.io/repos/github/yonkornilov/opus-api/
