.. role:: bash(code)
:language: bash

Usage
======

Installing the cdm package will set up a :bash:`cdm` executable.

Installing Datasets
---------------------

:bash:`cdm list` will provide a list of installable datasets and their descriptions.

:bash:`cdm install <dataset>` will install a specific dataset.  You may pass the :bash:`--graph` or :bash:`--search` flags to install DataStax Enterprise specific features.

Updating the local database
-----------------------------

:bash:`cdm update` will update the local database.


DSE Graph Support
------------------

Graphs can be enabled with the :bash:`--graph` flag.  It's up to the maintainer of the dataset to add graph support, and the DSE extensions for the Cassandra Driver must be installed.

DSE Search Support
--------------------

Coming soon.

Web Interface
-------------

Coming soon.

Streaming
------------

