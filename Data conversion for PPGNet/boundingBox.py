#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''--------Bounding box for clipping indivudual roofs-----------'''

import cv2 as cv
from coordinates import *

def boundingBox():
    x_min = 456000
    y_min = 5748000
    Individual_coord = coordinates()[0]

    pixel = []
    for i in range(len(Individual_coord)):
        x = []
        y = []
        for j in range(len(Individual_coord[i])):
            for k in range(2):
                x_pixel = int((Individual_coord[i][j][k][0] - x_min)*10)
                y_pixel = 10000 - int((Individual_coord[i][j][k][1] - y_min)*10)
                x.append(x_pixel)
                y.append(y_pixel)

        row, col = (len(x),2)
        pix = [[0]*col for y in range(row)]
        for i in range(len(x)):
            pix[i][0] = x[i]
            pix[i][1] = y[i]   
        pixel.append(pix) 
    #print(len(pixel))
    #print(pixel[0]) 
    
    def bounding_box(points):
        """returns a list containing the bottom left and the top right 
        points in the sequence
        Here, we use min and max four times over the collection of points
        """
        bot_left_x = min(point[0] for point in points)
        bot_left_y = min(point[1] for point in points)
        top_right_x = max(point[0] for point in points)
        top_right_y = max(point[1] for point in points)

        return [(bot_left_x, bot_left_y), (top_right_x, top_right_y)]
    bound_box = []
    for i in range(len(pixel)):
        bb = bounding_box(pixel[i])
        bound_box.append(bb)
    #print(bound_box[0])

    # Buffer
    bound_buffer_xtop = []
    bound_buffer_ytop = []
    bound_buffer_xbottom = []
    bound_buffer_ybottom = []
    for i in range(len(bound_box)):
        if  bound_box[i][0][0] < 20:         # one image was on the edge, so subtracting 20 would take the 
                                             # bounding box outside the image and error was seen. 
                                             # the clipped image of such roof omits some part of the roof
            x_topleft = bound_box[i][0][0]
        else:
            x_topleft = bound_box[i][0][0] - 20
        y_topleft = bound_box[i][0][1] - 20
        x_bottomright = bound_box[i][1][0] + 20
        y_bottomright = bound_box[i][1][1] + 20
        bound_buffer_xtop.append(x_topleft)
        bound_buffer_ytop.append(y_topleft)
        bound_buffer_xbottom.append(x_bottomright)
        bound_buffer_ybottom.append(y_bottomright)
    #print(bound_buffer_xtop)

    '''gives the two points of bounding box for each roof'''
    row, col = (len(bound_box), 4)
    buffer = [[0]*col for y in range(row)]
    for i in range(len(bound_box)):    
        for j in range(4):
            if j == 0:
                buffer[i][j] =bound_buffer_xtop[i]
            elif j == 1:
                buffer[i][j] =bound_buffer_ytop[i]
            elif j == 2:
                buffer[i][j] =bound_buffer_xbottom[i]
            else:
                buffer[i][j] =bound_buffer_ybottom[i]
    #print(buffer)
    #print(buffer[0])
    #print(len(buffer))
    return buffer


# In[ ]:




