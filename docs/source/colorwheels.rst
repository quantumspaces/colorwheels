***********
Colorwheels
***********

Introduction
============

A Color management module, containing the ``Colorwheel`` generator. As described in the code documentation, the idea of the colorwheel is to choose a sequence of colors, and, by using a ``next`` call, select the next color in the chain. Then start at the beginning again.

Our generator allows to multiple return types. You can tweak the return values by setting a ``generator_type`` to any one of those values: ``"rgb_tuple"``, ``"rgba_tuple"``, or ``"hexadecimal"``. If calling standard ``next`` methods, 3 are provided for each mentioned type of return value.

Specification
=============

.. automodule:: colorwheels.colorwheels
    :members:
    :special-members: __init__
