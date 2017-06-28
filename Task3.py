# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""

import numpy as np
import cv2
import os

path ='c:\\improc'
os.chdir(path)

im = cv2.imread('lena.jpg')
im2 = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

im2[:,:]=255-im2[:,:]
               
cv2.imshow('Lena negative',im2)
    
cv2.waitKey()
cv2.destroyAllWindows