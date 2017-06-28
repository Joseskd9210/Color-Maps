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

im[:,:,0]=0

cv2.imshow('Lena',im)

cv2.waitKey()
cv2.destroyAllWindows
