# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""
import numpy as np
import copy
import cv2
import os



path ='c:\\improc'
os.chdir(path)

im = cv2.imread('lena.jpg')

im2 = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#HUE
Hm = copy.copy(im2)
HM = copy.copy(im2)
#V = im2[:,:,2]

Hm[:,:,0] = 0
HM[:,:,0] = 255 

Hm = cv2.cvtColor(Hm, cv2.COLOR_HSV2BGR)
HM = cv2.cvtColor(HM, cv2.COLOR_HSV2BGR)

cv2.imshow('Lena Hue channel (minimum)',Hm)
cv2.imshow('Lena Hue channel (maximum)',HM)

Sm = copy.copy(im2)
SM = copy.copy(im2)

Sm[:,:,1] = 0 
SM[:,:,1] = 255 

Sm = cv2.cvtColor(Sm, cv2.COLOR_HSV2BGR)
SM = cv2.cvtColor(SM, cv2.COLOR_HSV2BGR)

cv2.imshow('Lena Saturation channel (minimum)',Sm)
cv2.imshow('Lena saturation channel (maximum)',SM)


Vm = copy.copy(im2)
VM = copy.copy(im2)

Vm[:,:,2] = 0 
VM[:,:,2] = 255 

Vm = cv2.cvtColor(Vm, cv2.COLOR_HSV2BGR)
VM = cv2.cvtColor(VM, cv2.COLOR_HSV2BGR)

cv2.imshow('Lena Value channel (minimum)',Vm)
cv2.imshow('Lena Value channel (maximum)',VM)



cv2.waitKey()
cv2.destroyAllWindows


