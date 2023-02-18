AWHA-SIP the open boradcast codec
===================================


The **AWAH_SIP-codec** is an open SIP client tailored for the needs of a broadcast facility. 
The project is based on PJSIP_.  and QT_. 

EBU_TECH_3326_ is considered a lot to reach good interopability with existing broadcast SIP products.
The codec can handle multiple SIP accounts and has an integrated audio routing matrix witch is capable of routing an summing the various audio signals coming from the local audio interfaces.
Accounts can have an attached call recorder and anouncement player to create an answering machine. 
Various GPI funcitions are added to the system to support intercom applications.


**AWAH_SIP-codec** runs on different plattforms and can be controlled over a websocket. A separate GUI application is provided to control the codec.
This GUI wil be repaced by a web gui in the future.

.. _PJSIP: https://www.pjsip.org/
.. _QT: https://www.qt.io/
.. _EBU_TECH_3326: https://tech.ebu.ch/docs/tech/tech3326.pdf



Check out the `AWAH-SIP_Codec` section for further information, including
how to `installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::
   :maxdepth: 2

   AWAH-SIP_Codec
   user manual
