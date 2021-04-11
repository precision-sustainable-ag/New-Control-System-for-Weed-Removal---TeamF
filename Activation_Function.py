import RPi.GPIO as GPIO
from time import sleep                  #load time controls in the form of sleep command

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

laser.start(100)
                                          #start duty cycle at 0 to ensure that laser begins off

def activation(t):                      #define activation code
    x = 1
    while x == 1:                      #begin on/off cycle loop
        GPIO.output(in1, GPIO.HIGH)      #turn laser on at full power by changing duty cycle to 100, should supply 3.3 v
        GPIO.output(in2, GPIO.LOW)
        sleep(t)                        #halt code for 2 seconds meaning laser will remain on
        GPIO.output(in1, GPIO.LOW)        #turn off laser by changing duty cycle back to zero
        GPIO.output(in2, GPIO.LOW)
        x = x + 1
    return
