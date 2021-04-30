import RPi.GPIO as GPIO
import time
from time import sleep                  

# this program is for manually testing or setting up the actuators




mode = 4

###########################################
###  1 = laser off 
###  2 = laser on
###  3 = laser on/off t=0.5
###  4 = bleed pump
###  5 = pump t=0.05
###  6 = pump t=0.06
###########################################



def laserOff():

    L1 = 13 #HI
    L2 = 6 #LOW

    GPIO.setmode(GPIO.BCM)                
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.output(L1, GPIO.LOW)              
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(L1, GPIO.LOW)
    return


def laserOn():

    L1 = 13 #HI
    L2 = 6 #LOW

    GPIO.setmode(GPIO.BCM)                
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.output(L1, GPIO.LOW)              
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)
    return



def activationP(t):
    in1 = 23
    in2 = 24                                
    en = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)              
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)              
    GPIO.output(in2, GPIO.LOW)              
    laser = GPIO.PWM(en, 1000)               
    laser.start(90.90)
    GPIO.output(in1, GPIO.HIGH)      
    GPIO.output(in2, GPIO.LOW)
    sleep(t)                        
    GPIO.output(in1, GPIO.LOW)        
    GPIO.output(in2, GPIO.LOW)
    return


def activationL(t):
    L1 = 13 #HI
    L2 = 6 #LOW

    GPIO.setmode(GPIO.BCM)                
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.output(L1, GPIO.LOW)              
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(L1, GPIO.LOW)
                                             
    return

    
    
    
    
    
    
    
if (mode==1):
    laserOff()
elif (mode==2):
    laserOn()
elif (mode==3):
    activationL(0.5)
elif (mode==4):
    activationP(5)
elif (mode==5):
    activationP(0.05)
elif (mode==6):
    activationP(0.06)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    