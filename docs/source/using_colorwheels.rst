******************
Using Colorwheels
******************

Introduction
============

This is a getting started guide, on using Colorwheels modules. As mentioned in the introduction, a :doc:`colorwheels` instance is an endless color sequence generator to drive changing colors in our RGB Led hardware.

Once you have covered the basics, check our tutorial page on :doc:`color_handling`.

Importing
=========

To import all ``colorwheels`` modules, simply add an import statement to your script.

.. code-block:: python

    import colorwheels

Using the generator
===================

We'll start using our generator with preset colors. Learn more in the next sections about changing colors and other features. For now, we'll simply use default settings.

The pre-defined generator endlessly rotates red, green and blue. By default, it also returns these colors in an RGB tuple. You can however get colors in other formats as well.

A minimal generator code could look like this:

.. code-block:: python

    # mywheels.py
    #
    # Colorwheel Generator Example 1

    import colorwheels

    wheels = colorwheels.Colorwheels()

    for i in range(5):
        print(next(wheels))

Your output can be similar to the below (note, if you log to console, there could be more output lines from the logger):

.. code-block:: bash

    $ python mywheels.py
    (255, 0, 0)
    (0, 255, 0)
    (0, 0, 255)
    (255, 0, 0)
    (0, 255, 0)
    $

Similarly, you can invoke one of several 'next' methods directly. See below:

.. code-block:: python

    # ...
    for i in range(5):
        print(wheels.next())

Changing Color Type
===================

The object returns different data formats, based on a type setting. You can receive RGB, RGBA or hexadecimal values per each iteration.

The following example iterates colors with hexadecimal output.

.. code-block:: python

    # mywheels.py
    #
    # Colorwheel Generator Example 2

    import colorwheels

    wheels = colorwheels.Colorwheels()

    # set generator type ("rgb_tuple" or "rgba_tuple" or "hexadecimal")
    wheels.set_generator_type("hexadecimal")

    for i in range(5):
        print(next(wheels))

With the below output:

.. code-block:: bash

    $ python mywheels.py
    #ff0000
    #00ff00
    #0000ff
    #ff0000
    #00ff00
    $


Check the next section to see how to work with colors: :doc:`color_handling`

Switching colorwheels
=====================

You can switch palettes on the run. Below is a more complete example of real-life usage. Say you have a button with an RGB led, and you want to rotate a few red tints when button is pressed, otherwise animate a green palette, if released. The trick is in the ``activate_colorwheel`` method, which locates a wheel by name and activates it.

.. code-block:: python

    # mywheels.py
    #
    # Colorwheel Generator Example 3

    import colorwheels
    import time

    wheels = colorwheels.Colorwheels()

    # load your color palettes here. For example 'reds' for red tints, 
    # 'greens' for green tints

    def button_pressed(self):
        # do some logic here, return True or False
        return True

    while(True):
        if button_pressed:
            wheels.activate_colorwheel("reds")
        else:
            wheels.active_wheel("greens")    

        color = next(wheels)
        # apply color to button / LED etc.
        time.sleep(1)


Where to next?
==============

There are other features where our generator will help you. Check the available functions of :doc:`colorwheels` and :doc:`colorwheels_config`, as well as the features in our color classes: :doc:`color_item` and :doc:`wheel_item`.

Below is an example of using a so far not-mentioned class method of :doc:`wheel_item` - ``wheel_complement``: as you'll find out in the documentation, the method copies over an existing wheel item and switches all colors to complementing colors. Comes in very useful for example, when you want to handle object colors with a well contrasting background.

.. code-block:: python

    # mywheels.py
    #
    # Colorwheel Generator Example 4

    import colorwheels
    import time

    text_wheel = colorwheels.Colorwheels()
    background_wheel = colorwheels.Colorwheels()

    # load your color palettes here. For example 'reds' for red tints, 
    # 'greens' for green tints. We're going to activate blue tints.

    text_wheel.activate_colorwheel("blues")
    # background wheel generates a new palette 'blues_complement'
    # the palette is local (i.e. not stored in the config singleton)
    background_wheel.active_wheel = colorwheels.WheelItem.wheel_complement(text_wheel.active_wheel)

    while(True):
        text_color = next(text_wheel)
        background_color = next(background_wheel)
        # write your text with obtained colors
        time.sleep(1)


Logging
=======

The package uses standard Python logging. Please configure according to your needs.
