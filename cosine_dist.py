"""
Author: Muhammet Ali Güldalı
"""


import numpy as np
import math

#x = np.arange(0,np.pi,0.0001)
#z = np.arange(0,1,1/20)
#y = np.cos(x)
#x_coord = z/y
#x = 0
#for i in range(20):
#    y = np.cos(x*np.pi)
#    x = x+y/20
#    print(x)
def get_cosine_distribution():
    y = np.arange(0,1,1/10)
    y = np.append(y,1)
    x = np.cos(y*np.pi/2)
    x = (x)/2
    flipped_x = np.flip(x)[1:]+0.5
    x = (x-0.5)*-1
    x = np.append(x,flipped_x)
    return(x)
