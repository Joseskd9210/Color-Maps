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

for i in [0,1,2]:
    im[:,:,i]=255-im[:,:,i]
    
cv2.imshow('Lena negative 1',im)
  
im[:,:,:]=255-im[:,:,:]           

cv2.waitKey()
cv2.destroyAllWindows