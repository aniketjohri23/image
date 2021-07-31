import cv2
import numpy as np


col=['green','blue','purple','red']
col_hsvub=[[80,255,255],[130, 255, 255],[170,255,255],[179, 255, 255]]
col_hsvlb=[[45,60,50],[90, 130,50],[130,130,50],[161, 155, 84]]

font=cv2.FONT_HERSHEY_COMPLEX



img=cv2.imread('1.png')
#img=cv2.resize(img,(700,400))
cv2.imshow('origunal image',img)



#contours

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', thresh)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print("Number of Contours found = " + str(len(contours)))





#image_copy = img.copy()
#cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
#cv2.imshow('None approximation', image_copy)

for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.009 * cv2.arcLength(cnt,True),True)
    cv2.drawContours(img,[approx],0,(100,150,200),2)

    n=approx.ravel()
    i=0
    for j in n:
        if(i%2==0):
            x=n[i]
            y=n[i+1]

            string=str(x)+" "+str(y)
            print(string)
            
            cv2.putText(img,string,(x,y),font,1,(255,255,0))
        i+=1

cv2.imshow('co',img)






cv2.waitKey(0)


cv2.destroyAllWindows()
