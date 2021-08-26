#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''Visualization of Line segments for entire image (tif file)'''

import cv2 as cv
from pixel import *
line_seg = pixel()

img = cv.imread("kriti.tif", cv.IMREAD_COLOR)

for i in range(len(line_seg)):
    for j in range(len(line_seg[i])):
        cv.line(img,(line_seg[i][j][0],line_seg[i][j][1]),(line_seg[i][j][2],line_seg[i][j][3]),(255,0,0),15)
        cv.drawMarker(img, (line_seg[i][j][0],line_seg[i][j][1]) ,(0,0,255), markerType=cv.MARKER_STAR, 
              markerSize=40, thickness=8, line_type=cv.LINE_AA)
cv.namedWindow('Image with junctions and Line segments', cv.WINDOW_NORMAL)
cv.imshow('Image with junctions and Line segments', img)
cv.waitKey(0)            
cv.destroyAllWindows()


# In[ ]:




