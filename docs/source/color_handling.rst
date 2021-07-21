**************
Color Handling
**************

Introduction
============

The default color configuration comes with one RGB sequence as a default in the configuration file. You can import color sequences from a YAML definition file 
as well, or you can define your own in code of course. This section describes how.

Color Objects
=============

Colorwheels introduces 2 objects to handle color definitions: :doc:`color_item`, :doc:`wheel_item` for one specific color generator. The base class - :doc:`colorwheels` - handles multiple generator defintions, and related operations: loading, swapping color schemes etc.

* :doc:`color_item` : this is a dataclass which captures RGB information, and handles color conversions. You can use it stand-alone, or you can use it in lists of colors. One of those special color lists is a 'wheel_item', described below.
* :doc:`wheel_item` : A wheel Item is a dataclass, which handles one named collection of colors. It contains a list of :doc:`color_item` objects and gives them a label. This is the base of one color definition.

YAML Definition
===============

The easiest way to define colors is the code your own YAML file. We have a whole section dedicated to YAML, read more in :doc:`yaml_definitions`.

TODO

Colors in code
==============

TODO