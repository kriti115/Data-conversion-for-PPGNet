#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''For clipping the images: clips and saves the clipped images in designated folder'''
import cv2 as cv
from boundingBox import *

buffer = boundingBox()

img3 = cv.imread("kriti.tif", cv.IMREAD_COLOR)

clip = 0
for i in range(len(buffer)):
    cropped = img3[buffer[i][1]: buffer[i][3],buffer[i][0]: buffer[i][2]]
    cv.namedWindow('Clipped Images', cv.WINDOW_NORMAL)
    cv.imwrite(r"K:\project PPGnet\Clipped Images\trial for git\clip_00{}.jpg".format(clip), cropped)
    clip += 1    
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




