import os

def coordConversion(pxX, pxY, n):
    #Input: A set of pixel locations of the targeted object.
    #Output: A set of gcode strings that will move the printer to the right 
    #"G0 X(A) Y(B) Z(C)" - Tells the acutator to move in to the destination (A,B,C). It will not always be a straight line.
    #"G1 X(A) Y(B) Z(C)" - Tells the actuator to move in a straight line to the destination (A,B,C), where A,B,C are absolute doubles.
    #"G2 X(A) Y(B) I(C) J(D)" - Tells the acutator to move clockwise from a center point to the end point (A,B), where A,B are absolute doubles and C,D are offsets of X and Y respectively of the center point.
    #"G3 X(A) Y(B) I(C) J(D)" - Tells the acutator to move counter-clockwise from a center point to the end point (A,B), where A,B are absolute doubles and C,D are offsets of X and Y respectively of the center point.
    #Initial Varaiables:
    cameraResolutionX =  1296 #Maximum X resolution of the Pixy2 Camera. Change this to desire resolution when chosen.
    cameraResolutionY = 976 #Maximum Y resolution of the Pixy2 Camera. Change this to desire resolution when chosen.
    maximumBedLen = 219.9 #Maximum Length (X and Y) of Printer Bed. Do not change.
    maximumBedHei = 199.9 #Maximum Height (Z) of Printer. Do not change.
    pixtoGX = maximumBedLen/cameraResolutionX 
    pixtoGY = maximumBedLen/cameraResolutionY
    if (pxX > cameraResolutionX):
        pxX = cameraResolutionX
    if (pxY > cameraResolutionY):
        pxY = cameraResolutionY
    #Metadata:
    codeStream = ""
    codeStream += ";TARGET_ID: " + str(n) + "\n"
    codeStream += ";PIXEL_X_TARGET LOCATION: " + str(pxX) + "\n"
    codeStream += ";PIXEL_Y_TARGET LOCATION: " + str(pxY) + "\n"

    #GCode:
    codeStream += "G90 ;Sets Coordinates to absolute positioning.\n"
    codeStream += "M140 S0 ;Ensures that the bed does not heat up or turn on.\n"
    codeStream += "M104 S0 ;Ensures that the actuator does not heat up.\n"
    codeStream += "G0 Z" + str(maximumBedHei) +"\n"
    codeStream += "G0 X" + str(pxX*pixtoGX) +" Y" + str(pxY*pixtoGY) +"\n"
    codeStream += "G0 Z" + str(99.9) +"\n"
    return codeStream #gcode strings


def createFile(pxL, pxW):
    #Creates the file that will hold the gcode strings.
    n = 0
    while (os.path.exists("TargetLoc"+str(n)+".gcode")):
           n += 1
    else:
        f = open("TargetLoc"+str(n)+".gcode","w")
        f.write(coordConversion(pxL,pxW, n))
        f.close()
    return

def roundRobinSch():
    #Premliminary variables and function go here.
    mode = 0
    #Mode 0: Camera Mode - Communicates with Camera to establish connection and waits for data to be sent.
    #Mode 1: Conversion Mode - Converts and Builds Gcode file to be sent to printer movement.
    #Mode 2: Movement Mode - Establish connection with printer and moves the actuator to the target location based on gcode file.
    #Mode 3: Pump Mode - Establish connection with pump system and sends a pulse to the actuator to eject suficient amount of solution.
    while (true):
        if (mode == 0):
            mode +=1
        elif (mode ==1):
            mode +=1
        elif (mode ==2):
            mode +=1
        elif (mode ==3):
            mode +=1
        else: ##Default Path.
            createFile(0,0)    
        ##Clean up routine when microcontroller s waiting for a response or data.
        
    return

def main():
    x = int(input("Enter the x-coordinate:"))
    y = int(input("Enter the y-coordinate:"))
    createFile(x,y)
    return

main()
