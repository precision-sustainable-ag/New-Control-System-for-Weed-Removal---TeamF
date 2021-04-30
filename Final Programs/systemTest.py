import os
import time
from printrun.printcore import printcore
from printrun import gcoder
#from Activation_Function import activation
# import RPi.GPIO as GPIO
#from time import sleep 


# This program is for manually moving the actuator


speed = 8000

#GPIO.setwarnings(False)

p = printcore("/dev/ttyUSB0",115200) #Establish connection with printer- Arguments:port name, Baud Rate
time.sleep(4)
p.send_now("G90")
#p.send_now("G28 F"+str(speed))
p.send_now("G0 Z20 F"+str(speed)); p.send_now("G0 X235 Y235 ")




# in1 = 23
# in2 = 24                                
# en = 25
# 
# L1 = 13 #HI
# L2 = 6 #LOW
# delay = 0.1
# 
# GPIO.setmode(GPIO.BCM)                #BCM = gpio 00..nn numbers
# GPIO.setup(L1, GPIO.OUT)
# GPIO.setup(L2, GPIO.OUT)
# GPIO.output(L1, GPIO.LOW)              #set first input to low side
# GPIO.output(L2, GPIO.LOW)

