import cv2
import numpy as np


col=['green','blue','purple','red']
col_hsvub=[[80,255,255],[130, 255, 255],[170,255,255],[179, 255, 255]]
col_hsvlb=[[45,60,50],[90, 130,50],[130,130,50],[161, 155, 84]]



img=cv2.imread('1.png')
img=cv2.resize(img,(700,400))
cv2.imshow('origunal image',img)

#crop
crop=img[0:200 , 0:350]

cv2.imshow('cropped',crop)




cv2.waitkey(10000)


cv2.destroyAllWindows()
