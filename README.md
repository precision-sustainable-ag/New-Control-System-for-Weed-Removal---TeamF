CROWS - Project 3: Control Remover of Weeds System  - Software Files

**All the software for this project should be run with Python3

Python Programs:
Brain.py: Contains main() function.

cord_grab.py: Uses pixycam libraries to retrieve object coordinates from camera; sorts and returns a 2D array of coordinates

cord_conv.py: Converts coordinates from camera plane to actuator plane

Activation_Function.py: Turns laser or pump on/off

actuatorTest.py: Used to set up and test actuators. Most importantly, used to “prime” fluid hoses

systemStart.py: Used to manually move actuator to starting position
     
Printrun Library:
Python Library that establishes the connection between the microcontroller and actuator movement system and sends G-Code commands to the connected system. This library requires dependencies, listed below, to be installed onto the microcontroller to run correctly. Refer to the documentation outlined below for more information on dependencies installation: https://github.com/kliment/Printrun#readme


For Windows: Pyserial, Pyreadline, Pycairo, Pyglet, Appdirs, Numpy, Cairosvg, Dbus, wxPython4

For Ubuntu/Debian: Python3-serial, Python3-numpy, Python3-libxml2, Python3-gi, Python3-dbus, Python3-psutil, Python3-cairosvg Python3-appdirs, Python3-wxgtk4.0, libpython3-dev, Cython3





Pixy Libraries:
To connect and use the Pixy2 camera with the RaspberryPi via USB, the libpixyusb2 library must be built. Before beginning build, make sure the default python version is set to Python3. Instructions can be found here:

https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:hooking_up_pixy_to_a_raspberry_pi

Then, build the libpixyusb2 python wrapper and run build_python_demos.sh as outlined here:

https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:building_libpixyusb_as_a_python_module_on_linux&s[]=python

Then, copy the files from the Python Programs folder into the pixy2/build/python_demos directory. Build the PixyMon software which will be used to load different object detection parameter files (plants.prm and dots.prm). Build instructions can be found here:

https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:installing_pixymon_on_linux


Device Operation:
Load appropriate parameter files into PixyMon software. Use plants.prm for plants.pdf and dots.prm for dots.pdf. It should be noted that these parameters will only target blue and red dots and will not identify objects in the top 1.5” of the platform when the platform is fully extended. Parameters only need to be loaded once. Close PixyMon. 

Run systemStart.py to initialize the actuator’s “home” position and send the actuator to its “start” position. The main() function will return the actuator to “start” after each successful run, so this only needs to be run initially after device is powered on or if it is halted without returning to “start”

If using the device in “pump” mode, open actuatorTest.py, set mode to “4” and run. This will run the pump for 5 seconds in order to bleed the hose of any air bubbles. Process can be repeated if needed.

Open Brain.py. This file contains the main() function used to operate the device. In the header of roundRobinSch() are a number of variables that can be changed to alter the operation of the device. These are described in detail in Brain.py. Importantly, Change actMode to “1” for Laser Actuator mode or “2” for Pump Actuator mode.


main() can then be run. “start” position is with the platform fully extended out toward the front of the machine. Detectable objects should be placed on the platform prior to running main().

If the system is ever halted unexpectedly, resulting in an actuator that will not turn off, run actuatorTest.py with mode set to “1” to turn laser off or “5” to turn pump off.
