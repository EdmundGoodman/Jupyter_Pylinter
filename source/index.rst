.. jupylint documentation master file, created by
   sphinx-quickstart on Sun Jun 20 19:49:24 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Jupylint's documentation!
=====================================

**This project is archived, and no longer under active development.**

*Please consider using [https://github.com/nbQA-dev/nbQA](https://github.com/nbQA-dev/nbQA) instead*

A simple tool to extract python code from a Jupyter notebook, and then run
:code:`pylint` on it for static analysis.

Installation
------------

The library package has been published on PyPI, so can be found here:
https://pypi.org/project/jupylint/, and can be installed as follows:

.. code-block:: python

    pip install jupylint

Requirements
------------

The :code:`pylint` package is required, as :code:`jupylint` merely provides a
wrapper around it for Jupyter notebooks.

Contents
--------

.. toctree::
   :maxdepth: 2

   project
   usage
   autodoc


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
