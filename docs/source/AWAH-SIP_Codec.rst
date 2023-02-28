AWAH-SIP_Codec
==============


The AWAH_SIP_Codec is a command line application that can be run as a daemon. The configuration is stored in a separate config file, this file is not editable.
To configure the codec you need the AWAH-SIP_GUI.

Installation compiled binary
----------------------------

The newest compiled version can be downloaded here: AWAH-SIP_Codec-download_.


.. _AWAH-SIP_Codec-download: https://github.com/AWAH-SIP/AWAH-SIP_Codec/actions

.. note::

   You ndeed to sign in to GitLab in order to see the and download the files.




Installation from soure
-----------------------


.. note::

   If you compile from source depening on the os some dependencies are required


`dependencies: opus` can be installed with brew_ on osx.

.. _brew: https://brew.sh/

.. code-block:: console

   brew install opus 


`dependencies: opus` can be installed on linux with the package manager.

.. _brew: https://brew.sh/

.. code-block:: console

   sudo apt-get install libopus-dev 



