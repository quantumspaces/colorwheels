*********
ColorItem
*********

Introduction
============

We keep color information and color logic together. **ColorItem** is a dataclass to simplify handling of color elements (RGB and others).

The class keeps native information about the RGB parts in dedicated fields. It can represent a color in one of the formats listed below.

* *RGB - ColorItem* instance: this is the native representation of a color
* *RGB - tuple*: You can retrieve color information as an RGB tuple. A red would become `(255, 0, 0)`

* *RGB - normalized tuple*: a color in some systems has to be represented by float values from 0 to 1. The normalized tuple can represent this. The red example would look as follows: `(1.0, 0.0, 0.0)`

* *RGBA - tuple*: PIL and others sometimes work with RGBA tuples. The color information is enriched with the Alpha information, in this release hardcoded as '255'. Our red would be represented as `(255, 0, 0, 255)`

* *RGB hexadecimal*: the color can be sent as an RGB hexadecimal string.

A few conversion color methods are bundled together with color information.

Specification
=============

.. automodule:: colorwheels.color_item
    :members:
