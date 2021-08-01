**************
Color Handling
**************

Introduction
============

The default color configuration comes with one RGB sequence as a default in the configuration file. You can import color sequences from a YAML definition file 
as well, or you can define your own in code of course. This section describes how.

Get more details on crafting your YAML file in this tutorial section: :doc:`yaml_definitions`.

Color Objects
=============

Colorwheels introduces 2 objects to handle color definitions: :doc:`color_item`, :doc:`wheel_item` for one specific color generator. The base class - :doc:`colorwheels` - handles multiple generator defintions, and related operations: loading, swapping color schemes etc.

* :doc:`color_item` : this is a dataclass which captures RGB information, and handles color conversions. You can use it stand-alone, or you can use it in lists of colors. One of those special color lists is a 'wheel_item', described below.
* :doc:`wheel_item` : A wheel Item is a dataclass, which handles one named collection of colors. It contains a list of :doc:`color_item` objects and gives them a label. This is the base of one color definition.

YAML Definition
===============

The easiest way to define colors is the code your own YAML file. We have a whole section dedicated to YAML, read more in :doc:`yaml_definitions`. You can also find an example color definition file in the examples directory.

Colors in code
==============

You may want to add a color definitions to the pool of available colors (which is managed by :doc:`colorwheels_config`). As soon as the color definition you create is added, it will be available to all :doc:`colorwheels` instances.

A color definition is basically a list of colors (defined by the :doc:`color_item` dataclass) with a name attached. This is bundled in the :doc:`wheel_item` dataclass.

So, adding your own RGB sequence using code could look like this:

.. code-block:: python

    # mywheels.py
    #
    # Colorwheel Generator Example 4

    from typing import List
    import colorwheels

    def my_rgb():
        """Create a list of colors (rgb)"""

        color_list = list()
        color_list.append(colorwheels.ColorItem(red=255, green=0, blue=0))
        color_list.append(colorwheels.ColorItem(red=0, green=255, blue=0))
        color_list.append(colorwheels.ColorItem(red=0, green=0, blue=255))

        return color_list

    wheels = colorwheels.Colorwheels()
    # add my new list named 'myrgb' to common configurations ->
    # can be used by any other instance of Colorwheels
    wheels.wheel_configurations.add_wheel_item(colorwheels.WheelItem("myrgb", my_rgb()))
