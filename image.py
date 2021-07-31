import cv2
import numpy as np


col=['green','blue','purple','red']
col_hsvub=[[80,255,255],[130, 255, 255],[170,255,255],[179, 255, 255]]
col_hsvlb=[[45,60,50],[90, 130,50],[130,130,50],[161, 155, 84]]



img=cv2.imread('1.png')
img=cv2.resize(img,(700,400))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,np.array(col_hsvlb[1]),np.array(col_hsvub[1]))

#imgr=cv2.rotate(img,rotateCode=0)

h,w,c=img.shape
center=(h//2,w//2)
rotation_matrix=cv2.getRotationMatrix2D(center,-15,1.0)
final_rotated=cv2.warpAffine(img,rotation_matrix,(w,h))


'''
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('img',img)
#cv2.imshow('rotated',final_rotated)
#cv2.waitKey(0)
'''
orig_img_coor=np.float32([[0,0],[1150,0],[0,647],[1131,647]])
pts=[[13,23],[1127,149],[13,639],[1129,569]]
for x in pts:
    cv2.circle(img,(x[0],x[1]),15,(255,0,0),-1)
#coordinated marked

cv2.imshow('coordinates marked',img)


height,width=800,800

new_img_coor=np.float32([[0,0],[600,0],[0,600],[600,800]])

P = cv2.getPerspectiveTransform(orig_img_coor ,new_img_coor)
perspective=cv2.warpPerspective(img,P,(width,height))

cv2.imshow('perspective',perspective)
cv2.waitkey(0)


cv2.destroyAllWindows()
