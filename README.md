# colorwheels

An Endless Color Generator

This project is a continuous color generator for Python. We create a palette of a specific color range, a palette of matching colors and similar to serve to a consumer application. 

Works great when generating rainbow effects in hobby electronics (RGB LEDs, RGB Panels), and elsewhere. The idea behind is an endless colorwheel for photographers - the wheel continuously turns around to generate the next color.

Here's an example of colorwheels on a keybow, waiting for a keypress.

![keybow](https://raw.githubusercontent.com/quantumspaces/colorwheels/0.7.2/img/keybow-colorwheels.gif)

All in a few lines of code:

```python

# wheel is initialized and definitions loaded or generated
while True:
    color = wheel.next()
    keybow.set_led(9, color[0], color[1], color[2])
    keybow.show()
    time.sleep(0.1)
```

similarly, we use colorwheels for generating color effects on RGB matrices. Below is an example of a rainbow colorwheel used for text, black colorwheel used for background and all captured from *ty-porter's* [RGBMatrixEmulator](https://github.com/quantumspaces/colorwheels/blob/006808d6656f2c8d4d97a08d90c797dbe240b6f8/img/welcome-rainbow.gif)

![rainbow welcome](img/welcome-rainbow.gif)

## Links

* [GitHub](https://github.com/quantumspaces/colorwheels)
* [PyPi](https://pypi.org/project/colorwheels/)
* [Read The Docs](https://colorwheels.readthedocs.io/en/latest/)

## About

We are a maker community in Karlskrona, Sweden. We run makerspaces every week, working with Raspberry Pis, Arduinos and other interesting hardware.

This repository is here to support our community of makers. A lot of our achievements are based and inspired by the community at large. We wish to pay back and share our experiences and lessons learned.
