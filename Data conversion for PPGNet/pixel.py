#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''Conversion of latitude longitude coordinates to Pixel coordinates'''

import cv2 as cv
from coordinates import *
    
def pixel():
    Individual_line = coordinates()[1]

    x_min = 456000     # minimum x coordinate of image from QGIS
    y_min = 5748000    # minimum y coordinate of image from QGIS

    pixel = [] # junction
    line_seg = [] # line segment
    for i in range(len(Individual_line)):
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for j in range(len(Individual_line[i])):
                x1_pixel = int((Individual_line[i][j][0] - x_min)*10)
                y1_pixel = 10000 - int((Individual_line[i][j][1] - y_min)*10)
                x2_pixel = int((Individual_line[i][j][2] - x_min)*10)
                y2_pixel = 10000 - int((Individual_line[i][j][3] - y_min)*10)
                x1.append(x1_pixel)
                y1.append(y1_pixel)
                x2.append(x2_pixel)
                y2.append(y2_pixel)

        row, col = (len(x1),4)
        line = [[0]*col for y in range(row)]
        for i in range(len(x1)):
            line[i][0] = x1[i]
            line[i][1] = y1[i]   
            line[i][2] = x2[i]
            line[i][3] = y2[i]
        line_seg.append(line) 

    return line_seg
    #print(len(line_seg))
    #print(line_seg[0]) #line segment for one roof
    #print(line_seg[0][0])

