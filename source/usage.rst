Example Usage
=============

Importing the module
--------------------

.. code-block:: python

    from jupylint import Jupylint


Linting a file from within python
---------------------------------

.. code-block:: python

    args = {
        "in_file_name": ['./in.ipynb'],
        "out_file_name": './out.py',
        "save_file": True
    }
    result = Jupylint.execute(args)
    print(result)


Linting a file from the command line
------------------------------------

.. code-block:: bash

    python jupylint.py ./in.ipynb


Getting help from the command line
----------------------------------

.. code-block:: bash

    python jupylint.py --help
