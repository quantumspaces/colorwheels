# mywheels.py
#
# Colorwheel Generator Example 2

import colorwheels

wheels = colorwheels.Colorwheels()

# set generator type ("rgb_tuple" or "rgba_tuple" or "hexadecimal")
wheels.set_generator_type("hexadecimal")

for i in range(5):
    print(next(wheels))
