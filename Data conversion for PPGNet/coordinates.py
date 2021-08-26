#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import numpy as np
import cv2 as cv

'''Understaning the data and seperating junctions and line segments for individual roofs'''

'''---------------Loading GeoJSON files----------------'''
def coordinates():
    with open("Kriti_456_5748.geojson",'r') as f:
        data = json.loads(f.read())

    '''----------------Reading the coordinates--------------'''

    coord_per_building = []
    for i in range(len(data['features'])):
        coordinates = data['features'][i]['geometry']['coordinates']
        coord_per_building.append(coordinates)
    #print(coord_per_building[0]) # for building (id = 0)
    #print(len(coord_per_building))

    '''---------Separating start and end coordinates---------'''

    Individual_coord = [] # coordinates of junctions
    Individual_line = [] # coordinates of line segments
    for i in coord_per_building:
        start_coord = []
        end_coord = []
        for j in range(len(i)):
            for k in range (len(i[j])-1): 
                start = i[j][k]
                end = i[j][k+1]
                start_coord.append(start)
                end_coord.append(end)

        '''-------Start and end coordinates: Junctions (x,y)-------'''

        row, col = (len(start_coord),2)
        individual_coord = [[0]*col for y in range(row)]
        for i in range(len(start_coord)):
            individual_coord[i][0] = start_coord[i]
            individual_coord[i][1] = end_coord[i]
        Individual_coord.append(individual_coord)

        '''---Line segement- quadruples from above junctions (x1,y1,x2,y2)---'''

        row, col = (len(start_coord),4)
        individual_line = [[0]*col for y in range(row)]
        for i in range(len(start_coord)):
            individual_line[i][0] = start_coord[i][0]
            individual_line[i][1] = start_coord[i][1]
            individual_line[i][2] = end_coord[i][0]
            individual_line[i][3] = end_coord[i][1]
        Individual_line.append(individual_line)    

    '''---------For understanding the results---------'''    

    '''print(start_coord, '\n')
    print(end_coord, '\n')

    print(Final_individual_coord[0]) # for individual roofs
    print(len(Final_individual_coord))

    print(Final_individual_line[0]) # for individual roofs
    print(len(Final_individual_line))'''
    return Individual_coord, Individual_line


# In[11]:


coord = coordinates()[0]
coord


# In[13]:


line = coordinates()[1]
line


# In[ ]:


'''Conversion of latitude longitude coordinates to Pixel coordinates'''

from coordinates import *

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
    
#print(len(line_seg))
#print(line_seg[0]) #line segment for one roof
#print(line_seg[0][0]) 

'''Visualization of Line segments for entire image (tif file)'''

img = cv.imread("filename.tif", cv.IMREAD_COLOR)

for i in range(len(line_seg)):
    for j in range(len(line_seg[i])):
        cv.line(img,(line_seg[i][j][0],line_seg[i][j][1]),(line_seg[i][j][2],line_seg[i][j][3]),(255,0,0),15)
        cv.drawMarker(img, (line_seg[i][j][0],line_seg[i][j][1]) ,(0,0,255), markerType=cv.MARKER_STAR, 
              markerSize=40, thickness=8, line_type=cv.LINE_AA)
cv.namedWindow('Image with junctions and Line segments', cv.WINDOW_NORMAL)
cv.imshow('Image with junctions and Line segments', img)
#cv.waitKey(0)            
#cv.destroyAllWindows()

