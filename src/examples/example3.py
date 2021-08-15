# mywheels.py
#
# Colorwheel Generator Example 3

import colorwheels
import time

wheels = colorwheels.Colorwheels()

# load your color palettes here. For example 'reds' for red tints, 
# 'greens' for green tints
conf = colorwheels.ColorwheelsConfig()
conf.load_wheels("basic_wheels.yml")

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
