Usage
=====

.. _AWAH-SIP_Codec:

Installation Linux
------------------

To use AWAH-SIP, first install it:

.. code-block:: console

   Clone Repo
Run git submodules init && git submodule update after cloning this repo to load the AWAH-SIP_Library from it's own Repo!

Installation OS X
-----------------


Installation Windows
--------------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

