# mywheels.py
#
# Colorwheel Generator Example 1

import colorwheels

wheels = colorwheels.Colorwheels()

for i in range(5):
    print(next(wheels))
