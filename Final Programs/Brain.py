import os
import time
from printrun.printcore import printcore
from printrun import gcoder
from cord_grab import coordinates
from Activation_Function import activationL, activationP
from cord_conv import coordConversion
import RPi.GPIO as GPIO


# This requires the Printcore Module to work.
# Follow Instructions here to install: https://github.com/kliment/Printrun
# WARNING: DO NOT RUN IF THE PRINTER MOTOR IS NOT PLUGGED IN.



def remTargetfiles():
    #Removes previous gcode files from Targets folder.
    n = 1
    while (os.path.exists("./targets/TargetLoc"+str(n)+".gcode")):
        os.remove("./targets/TargetLoc"+str(n)+".gcode")
        n +=1
    return

def createFile(pxL, pxW, mode):
    #Creates the file that will hold the gcode strings.
    n = 1
    while (os.path.exists("./targets/TargetLoc"+str(n)+".gcode")):
           n += 1
    else:
        f = open("./targets/TargetLoc"+str(n)+".gcode","w")
        f.write(coordConversion(pxL,pxW, n, mode))
        f.close()
    return

def createLog():
    #Creates the file that will hold the camera's coordinates.
    f = open("./targets/LogTargets.txt","w")
    f.write("#:|x:|y:\n")
    f.close()
    return

def populateLog(pArray):
    #Populates the log file with camera's coordinates given by the pixycam.
    f = open("./targets/LogTargets.txt","a")
    n = int(pArray[0][0])
    print("Amount of Detected Targets: " + str(n) + "\n")
    for i in range(1,n+1):
        x = str(pArray[i][0])
        #print("x:" + x + "\n")
        y = str(pArray[i][1])
        #print("y:" + y + "\n")
        f.write(str(i) +":|" + x + "|" + y + "\n")
    f.close()
    return


def roundRobinSch():

    actMode = 2 # 1 for Laser, 2 for pump
    lamp = 0 #controls pixy lamp during cord_grab() call 0=off 1=half brightness, 2=full brightness
    lTime = 0.5 #time lamp stays on when lamp==1 or lamp==2
    iniDelay = 2 #wait time for starting movements
    pumTime = 0.05 #activation time for pump
    
    
    mode = 0 #Starting mode for Round Robin
    GPIO.setwarnings(False)
        
    posZ = 20 #operation Height of actuator
    speed = 8000 #speed setting for stepper motors
    numCords = 20 #size of coordinate array
    lasTime = 0.5 #activation time for laser
    actDelay = 0.5 #wait time for after activation
      
        
    #Mode 0: Camera Mode - Communicates with Camera to establish connection and waits for data to be sent.
    #Mode 1: Conversion Mode - Converts and Builds Gcode file to be sent to printer movement.
    #Mode 2: Movement Mode - Establish connection with printer and moves the actuator to the target location based on gcode file.
    #Mode 3: Actuator Mode - Establish connection with pump system and sends a pulse to the actuator to eject suficient amount of solution.
    p = printcore("/dev/ttyUSB0",115200) #Establish connection with printer- Arguments:port name, Baud Rate
    time.sleep(4)
    print("Printer is now online.")
    p.send_now("G90")
    #p.send_now("G28 F"+str(speed))
    p.send_now("M92 X80 y80")
    #p.send_now("G0 Z"+str(posZ)+" F"+str(speed))
    p.send_now("G0 X234.9 Y234.9 Z"+str(posZ)+" F"+str(speed))
    print("...Waiting")
#     for j in range (0,iniDelay):
#         print(iniDelay-j)
#         time.sleep(1)
    time.sleep(iniDelay)
    
    n = 1
    remTargetfiles() 
    createLog()
    pixyArray = coordinates(numCords, actMode, lamp, lTime); #Calls PixyCam's function and returns array.
    populateLog(pixyArray) #Populate Log File with PixyCam's Coords.
    
    while (True):
        
        if (mode == 0):
            print("Coordinate Read MODE")
            if ((int(pixyArray[n][0]) == 0) and (int(pixyArray[n][1]) == 0)):
                 break
            x = int(pixyArray[n][0])
            y = int(pixyArray[n][1])
            n += 1
            mode +=1
            
            
        elif (mode ==1):
            print("Coordinate Conversion MODE")
            print("Point #" + str(n-1)+"\n")
            createFile(x,y, actMode)
            gcode= [i.strip() for i in open("./targets/TargetLoc"+str(n-1)+".gcode")]
            gcode1= gcoder.LightGCode(gcode)
            mode +=1
            
            
        elif (mode ==2):
            print("Movement MODE")
            #SEND code file to printer
            p.startprint(gcode1)
            #time.sleep(2)
            #while (position == False):
            #    position = checkPos()
            time.sleep(1) #At least one second needs to pass before the function is called.
            while (p.endChecker()): #Function call that returns true or false whether the actuator movement system is running gcode.
                #time.sleep(1)
                continue
            mode +=1
            
            
        elif (mode ==3):
            if (actMode == 1):
                print("Laser MODE")
                print("\nLaser On")
                activationL(lasTime)
                print("Laser Off\n")
                time.sleep(actDelay)
                mode +=1
            elif (actMode == 2):
                print("PUMP MODE")
                print("\nPump On")
                activationP(pumTime)
                print("Pump Off\n")
                time.sleep(actDelay)
                mode +=1
            
            
        else: ##Default Path.
            #Resets Round-Robin Scheduler
            mode = 0
        ##Clean up routine when microcontroller is waiting for a response or data.
    print("Process Complete!\n")
    p.send_now("G1 X235 Y235 Z"+str(posZ)+" F"+str(speed))
    return

def main():
    roundRobinSch() #Remove first "#" to run the Round Robin Scheduler.
    return

main()
