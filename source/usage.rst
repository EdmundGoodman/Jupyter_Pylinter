Example Usage
=============

Importing the module
--------------------

.. code-block:: python

    from jupylint import Jupylint


Linting a file from the command line
------------------------------------

.. code-block:: bash

    jupylint <in.ipynb>


Saving the raw python extracted from the notebook for linting
-------------------------------------------------------------

.. code-block:: bash

    jupylint -k <in.ipynb>
    jupylint --keep <in.ipynb>

    # The destination of the saved file can also be specified:
    jupylint --keep <in.ipynb> <out.py>


Specifying a custom pylintrc file
---------------------------------

.. code-block:: bash

    jupylint <in.ipynb> --rcfile <pylintrc>


Getting the version number
--------------------------

.. code-block:: bash

    jupylint -v
    jupylint --version


Getting help from the command line
----------------------------------

.. code-block:: bash

    jupylint -h
    jupylint --help


Linting a file from within python
---------------------------------

.. code-block:: python

    # First, we need to import the module
    from jupylint import Jupylint

    # The most common use case within python is likely to be manually
    # specifying the parameters to run the tool with.
    # All three dictionary keys below are required, but there is an additional
    # optional one "rcfile", which specifies the location of a pylintrc file
    args = {
        "in_file_name": ['./in.ipynb'],
        "out_file_name": './jupylint_tmp_out.py',
        "save_file": True
    }
    result = Jupylint.execute(args)
    print(result)

    # Additionally, if the settings are already present as keyword arguments,
    # for example using `python - ./in.ipynb`, the tool can be run on those
    # arguments using:
    Jupylint.run()
