#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Calculates the pixels for indiviudal (clipped) images'''
from pixel import *
from boundingBox import *

def individualLineSegment():
    line_seg = pixel()
    buffer = boundingBox()

    line_clipped = [] # contains the line segment for each individual roof
    for i in range(len(line_seg)): 
        dist_x1 = []
        dist_y1 = []
        dist_x2 = []
        dist_y2 = []  
        for k in range(len(line_seg[i])): 
            distance_x1 = line_seg[i][k][0] - buffer[i][0] # pixel coordinates - buffer (only the minimum buffer is used)
            distance_y1 = line_seg[i][k][1] - buffer[i][1]
            distance_x2 = line_seg[i][k][2] - buffer[i][0] # pixel coordinates - buffer (only the minimum buffer is used)
            distance_y2 = line_seg[i][k][3] - buffer[i][1]
            dist_x1.append(distance_x1)
            dist_y1.append(distance_y1)
            dist_x2.append(distance_x2)
            dist_y2.append(distance_y2)

        row, col = (len(dist_x1), 4)
        indivisual_line = [[0]*col for y in range(row)]
        for j in range(len(dist_x1)):
            indivisual_line[j][0] = dist_x1[j]
            indivisual_line[j][1] = dist_y1[j]
            indivisual_line[j][2] = dist_x2[j]
            indivisual_line[j][3] = dist_y2[j]
        line_clipped.append(indivisual_line)
    #print(len(line_clipped))
    #print(line_clipped)
    return line_clipped

