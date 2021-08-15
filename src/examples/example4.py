# mywheels.py
#
# Colorwheel Generator Example 4

import colorwheels
import time

text_wheel = colorwheels.Colorwheels()
background_wheel = colorwheels.Colorwheels()

# load your color palettes here. For example 'reds' for red tints, 
# 'greens' for green tints.
conf = colorwheels.ColorwheelsConfig()
conf.load_wheels("basic_wheels.yml")

# We're going to activate blue tints.
text_wheel.activate_colorwheel("blues")

# background wheel generates a new palette 'blues_complement'
# the palette is local (i.e. not stored in the config singleton)
background_wheel.active_wheel = colorwheels.WheelItem.wheel_complement(text_wheel.active_wheel)

while(True):
    text_color = next(text_wheel)
    background_color = next(background_wheel)
    # write your text with obtained colors
    time.sleep(1)
