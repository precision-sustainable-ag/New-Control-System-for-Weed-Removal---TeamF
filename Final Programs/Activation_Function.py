
import RPi.GPIO as GPIO
import time
from time import sleep                  #load time controls in the form of sleep command




# activationP() is called for pump, activationL() is called for laser




def activationP(t):
    in1 = 23
    in2 = 24                                #enable 3 input pins necessary for L298N operation. in1 and in2 determine polarity of motor. en determines power delivered
    en = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)              #setup L298N pins corresponding to necessary Raspberri Pi pins
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)              #set first input to low side
    GPIO.output(in2, GPIO.LOW)              #set second input to high side
    laser = GPIO.PWM(en, 1000)               #setup up pulse width modulation control for laser out of 100
    laser.start(90.90)    
                                         

                                        #define activation code
    x = 1
    while x == 1:                      #begin on/off cycle loop
        GPIO.output(in1, GPIO.HIGH)      #turn laser on at full power by changing duty cycle to 100, should supply 3.3 v
        GPIO.output(in2, GPIO.LOW)
        sleep(t)                        #halt code for 2 seconds meaning laser will remain on
        GPIO.output(in1, GPIO.LOW)        #turn off laser by changing duty cycle back to zero
        GPIO.output(in2, GPIO.LOW)
        x = x + 1
    return


def activationL(t):
    L1 = 13 #HI
    L2 = 6 #LOW

    GPIO.setmode(GPIO.BCM)                #BCM = gpio 00..nn numbers
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.output(L1, GPIO.LOW)              #set first input to low side
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(L1, GPIO.LOW)
                                             
    return

    
