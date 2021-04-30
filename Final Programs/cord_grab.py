
import math
import numpy
import pixy
import time
from time import sleep
from ctypes import *
from pixy import *


# This code retrieves a single instance of detected objects via the pixy camera, sorts those objects across the y-axis, 
# and returns a 2D array of coordinates



def coordinates(numCords, mode, lamp, lTime): #numCords is size of coordinate array, mode =1 for laser, =2 for pump
    pixy.init ()
    pixy.change_prog ("color_connected_components");

    class Blocks (Structure):
        _fields_ = [ ("m_signature", c_uint),
        ("m_x", c_uint),
        ("m_y", c_uint),
        ("m_width", c_uint),
        ("m_height", c_uint),
        ("m_angle", c_uint),
        ("m_index", c_uint),
        ("m_age", c_uint) ]

    if (mode == 1): #LASER MODE
        Xmin = 80
        Xmax = 245
        Ymin = 0
        Ymax = 143
    elif (mode == 2): #PUMP MODE
        Xmin = 65
        Xmax = 245
        Ymin = 0
        Ymax = 143

    blocks = BlockArray(100)
    frame = 0
    sz=numCords #size of coordinate array
    
    
    if (lamp==1):
        set_lamp(1,0)
        count = pixy.ccc_get_blocks (100, blocks)
        time.sleep(lTime)
        set_lamp(0,0)
    elif(lamp==2):
        set_lamp(1,1)
        count = pixy.ccc_get_blocks (100, blocks)
        time.sleep(lTime)
        set_lamp(0,0)
    elif(lamp==0):
        count = pixy.ccc_get_blocks (100, blocks)




    n = 0
    temp = numpy.zeros((sz,2))
    
    for k in range (1, count): 
        X = blocks[k].m_x #retreive x and y coordinates of block centerpoint
        Y = blocks[k].m_y
        if X>Xmin and X<Xmax and Y>Ymin and Y<Ymax: #check for ROI
            temp[n] = (Y,X-Xmin) #arrange cords in (Y,X) for sorting by Y
            n+=1
    
    order = numpy.argsort(temp,0) #create sort order array
    index = numpy.zeros((sz,2))
    cords = numpy.zeros((sz+1,2)) #array to hold sorted coordinates
    cords[0,0] = n #first item in coordinate array is number of coordinates
    

    #arranges coordinates acording to values in order[]
    for k in range (0,sz):
        cords[sz-k,:] = temp[order[k,0],:]
    
    
    cords[1:, [0,1]] = cords[1:,[1,0]] #switch cords from (Y,X) to (X,Y)
    cords = cords.astype(numpy.int) #change cords[] to integer array
   
    
    #print('count', count)
    print('number', n)
    #print('\ntemp\n', temp)
    #print('order\n', order)
    print('cords\n',cords)
    
    
    return cords


#cords = coordinates(20,2)















