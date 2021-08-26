#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''------------Visualization of Bounding box------------'''

import cv2 as cv
from boundingBox import *

bound_box = boundingBox()

img1 = cv.imread("kriti.tif", cv.IMREAD_COLOR)
for i in range(len(bound_box)):
    cv.rectangle(img1,(bound_box[i][0],bound_box[i][1]),(bound_box[i][2],bound_box[i][3]),(255,0,0),15)

cv.namedWindow('Image with Bounding Box', cv.WINDOW_NORMAL)
cv.imshow('Image with Bounding Box', img1)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




