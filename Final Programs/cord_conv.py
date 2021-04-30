

def coordConversion(pxX, pxY, n, mode):
    #Input: A set of pixel locations of the targeted object.
    #Output: A set of gcode strings that will move the printer to the right 
    #"G0 X(A) Y(B) Z(C)" - Tells the acutator to move in to the destination (A,B,C). It will not always be a straight line.
    #"G1 X(A) Y(B) Z(C)" - Tells the actuator to move in a straight line to the destination (A,B,C), where A,B,C are absolute doubles.
    

    #Initial Varaiables:
    
    if (mode == 1): #LASER MODE
        pxResX =  168 #Maximum X resolution of the Pixy roi
        pxResY =  143 #Maximum Y resolution of the Pixy roi
        
        ptrMinX = 19 #X and Y bounds for printer, as seen by camera
        ptrMaxX = 235
        ptrMinY = 45
        ptrMaxY = 228 #when y=235 (plate fully extended, this is the highest point the camera can see

    elif (mode == 2): #PUMP MODE
        pxResX =  180 #Maximum X resolution of the Pixy roi
        pxResY =  143 #Maximum Y resolution of the Pixy roi
        
        ptrMinX = 0 #X and Y bounds for printer, as seen by camera
        ptrMaxX = 232
        ptrMinY = 49
        ptrMaxY = 232 #when y=235 (plate fully extended, this is the highest point the camera can see
        
    
    
    maximumBedLen = 234.9 #Maximum Length (X and Y) of Printer Bed. Do not change.
    maximumBedHei = 199.9 #Maximum Height (Z) of Printer. Do not change.
    
    ratioX = (ptrMaxX - ptrMinX)/pxResX #ratios for converting pxy to printer coordinates
    ratioY = (ptrMaxY - ptrMinY)/pxResY
    
    if (pxX > pxResX):
        pxX = pxResX
    if (pxY > pxResY):
        pxY = pxResY
        
    x = pxResX-pxX #X cord has to be flipped first
    x = x*ratioX #converted to printer coordinates
    x = x+ptrMinX #Then offset by boundary position of printer
    
    y = pxY*ratioY #these are same as for x but w/o flipping
    y = y+ptrMinY
    
        
    #Metadata:
    codeStream = ""
    #codeStream += ";TARGET_ID: " + str(n) + "\n"
    #codeStream += ";PIXEL_X_TARGET LOCATION: " + str(pxX) + "\n"
    #codeStream += ";PIXEL_Y_TARGET LOCATION: " + str(pxY) + "\n"

    #GCode:
    codeStream += "G90 ;Sets Coordinates to absolute positioning.\n"
    codeStream += "M140 S0 ;Ensures that the bed does not heat up or turn on.\n"
    codeStream += "M104 S0 ;Ensures that the actuator does not heat up.\n"
    #codeStream += "G0 Z" + str(maximumBedHei) +"\n"
    codeStream += "G0 X" + str(x) +" Y" + str(y) +"\n"
    codeStream += "M114\n" #Must be included at the end of the gcode for endChecker function to work.
    #codeStream += "G0 Z" + str(99.9) +"\n"
    return codeStream #gcode strings
