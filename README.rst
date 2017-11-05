Hangman
=======

.. image:: https://travis-ci.org/mos-polytech/hangman.svg?branch=master
    :target: https://travis-ci.org/mos-polytech/hangman
.. image:: https://coveralls.io/repos/github/mos-polytech/hangman/badge.svg?branch=master
    :target: https://coveralls.io/github/mos-polytech/hangman?branch=master

This is a hangman game written by @sobolevn.


Installation
------------

0. Create ``virtualenv``
1. Run ``python setup.py install``
2. Run ``hangman new``


Testing
-------

We don't have any tests yet.

How to run:

0. ``pipenv install --dev`` (only once)
1. ``pipenv shell``
2. ``pytest``


Type checking
-------------

How to run:

0. ``pipenv install --dev`` (only once)
1. ``pipenv shell``
2. ``mypy --strict-optional hangman``
