**********************
YAML Color Definitions
**********************

Introduction
============

Defining a color sequence in code is tedious. Definining more sequences even more so. Our package depends on color definitions coming from a YAML file.

This page describes the structure of such a file.

Specification
=============

One or more color definitions are located in a YAML file, defining color sequences used in your program.

YAML structure
--------------

The base YAML structure is as follows:

.. code-block:: yaml

    meta:
        release: "0.5.0.0"
    wheels:
        - wheel:
            name: "white"
            colors:
                - rgb: [255, 255, 255]
        - wheel:
            name: "RGB"
            colors:
                - rgb: [255, 0, 0]
                - rgb: [0, 255, 0]
                - rgb: [0, 0, 255]
        ...

The structure contains 2 segments:

* **meta** - containing metadata about the file, version (for compatibility reasons) and similar. In the current release, this section is ignored.
* **wheels** - a list of different (named) colorwheels. Each colorwheel item is defined within a *wheel* section.

Wheel Definitions
-----------------

Wheels can be represented in several ways, depending on the color effect we want to achieve. Generally, we have 2 types of *wheel* elements: listed, or calculated.

For example:

.. code-block:: yaml

    ...
    - wheel:
        name: "long-rainbow"
        type: "rainbow"
        size: 64
        amplitude: 127
        center: 128
        frequency: 0.3
    - wheel:
        name: "RGB"
        type: "sequence" # default value, need not be specified
        colors:
            - rgb: [255, 0, 0]
            - rgb: [0, 255, 0]
            - rgb: [0, 0, 255]
    ...

Above, we can see a standard RGB sequence, plus a 'calculated' sequence from parameters. The differentiator is the **type** field. This field identifies what to do with parameters, and defaults to **sequence**.

If you load the above definition into :class:`Colorwheels` (using the :class:`ColorwheelsConfig` ``load_wheels`` method), there will be 2 named color wheels you can switch back and forth.

Wheel types
-----------

sequence
^^^^^^^^

Sequence is the basic type of a wheel, and if not specified, this type becomes the default value. A 'sequence' contains a 'colors' list, where every list item is defined by it's RGB elements.

Below a usage example:

.. code-block:: yaml

    ...
    - wheel:
        name: "RGB"
        type: "sequence" # default value, need not be specified
        colors:
            - rgb: [255, 0, 0]
            - rgb: [0, 255, 0]
            - rgb: [0, 0, 255]
    ...


rainbow
^^^^^^^

Rainbow is a generated wheel. You specify how many elements to use, plus some algorithm parameters. You can generate rainbow sequences without really looking into the detail of the implementation: just specify 'size' (i.e. number of colors) and leave the rest to defaults.

Below a rainbow wheel:

.. code-block:: yaml

    ...
    - wheel:
        name: "my-rainbow"
        type: "rainbow"
        size: 32        # default value, need not be specified
        amplitude: 127  # default value, need not be specified
        center: 128     # default value, need not be specified
        frequency: 0.3  # default value, need not be specified
    ...

