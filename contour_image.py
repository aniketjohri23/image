import cv2
import numpy as np
import math


col=['green','blue','purple','red']
col_hsvub=[[80,255,255],[130, 255, 255],[170,255,255],[179, 255, 255]]
col_hsvlb=[[45,60,50],[90, 130,50],[130,130,50],[161, 155, 84]]

font=cv2.FONT_HERSHEY_COMPLEX

def perspective_fnx1(img_name):
    print("Loading image " + img_name)
    img=cv2.imread(img_name)
    #img=cv2.resize(img,(700,400))
    # cv2.imshow('origunal image',img)
    w,h = img.shape[0], img.shape[1]

    # print(w,h)

    #contours

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary image', thresh)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    # print("Number of Contours found = " + str(len(contours)))


    #image_copy = img.copy()
    #cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    #cv2.imshow('None approximation', image_copy)

    #Now this loop only finds the required contour
    area = 0
    pts = []
    n = []
    for cnt in contours:
        approx=cv2.approxPolyDP(cnt,0.009 * cv2.arcLength(cnt,True),True)
        # cv2.drawContours(img,[approx],0,(100,150,200),2)

        i=0
        # print(f"Area {cv2.contourArea(cnt)}")
        
        if (area < cv2.contourArea(cnt) and cv2.contourArea(cnt) < w * h * 0.95 and len(approx.ravel()) == 8):
                area = cv2.contourArea(cnt)
                pts = approx
                n=approx.ravel()
        
    #Required Contours and its points are drawn
    if len(pts) == 0:
        print("No contours found")
    else:
        cv2.drawContours(img,[pts],0,(100,150,200),2)
        # print(n)
        #Processing contours
        for j in n:
            if(i%2==0):
                x=n[i]
                y=n[i+1]

                string=str(x)+" "+str(y)
                # print(string)
                
                cv2.putText(img,string,(x-100,y),font,0.5,(255,255,0))
                
            i+=1
            
        cv2.imshow('co',img)

        #perspective tranformation

        #making two matrix of only x_coords and y_coords
        x = np.zeros(len(pts), dtype=int)
        y = np.zeros(len(pts), dtype=int)
        for _ in range(len(pts)):
            x[_] =  pts[_][0][0]
            y[_] =  pts[_][0][1]
        # print("hello",x,y)
        print("Changing Perspective")
        # srcTri = np.array( [[x[0],y[0]],
        #                     [x[1],y[1]],
        #                     [x[3],y[3]]] ).astype(np.float32)
        # dstTri = np.array([[x[0],y[0]],
        #                     [x[2],y[0]],
        #                     [x[0],y[2]]] ).astype(np.float32)
        src2Tri = np.array( [[x[0],y[0]],
                            [x[1],y[1]],
                            [x[2],y[2]],
                            [x[3],y[3]]] ).astype(np.float32)

        w_per = int((math.sqrt((y[0]-y[1])**2 + (x[0]-x[1])**2) + 
                            math.sqrt((y[2]-y[3])**2 + (x[2]-x[3])**2))/2)

        h_per = int((math.sqrt((y[2]-y[1])**2 + (x[2]-x[1])**2) + 
                            math.sqrt((y[0]-y[3])**2 + (x[0]-x[3])**2))/2)

        dst2Tri = np.array([[0,0],
                            [w_per,0],
                            [w_per,h_per],
                            [0,h_per]] ).astype(np.float32)

        # warp_mat = cv2.getAffineTransform(srcTri, dstTri)
        # warp_starter = img.copy()
        # warp_dst = cv2.warpAffine(warp_starter, warp_mat, (warp_starter.shape[1], warp_starter.shape[0]))
        # print(h_per,w_per)
        perspective_mat =  cv2.getPerspectiveTransform(src2Tri, dst2Tri)
        perspective_starter = img.copy()
        perspective_dst = cv2.warpPerspective(perspective_starter, perspective_mat,(w_per,h_per))
        print("Displaying changed perspective image...")
        cv2.imshow('kaboom',perspective_dst)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == '__main__':
    img1 = '1.png'
    img2 = '3.png'
    perspective_fnx1(img1)
    perspective_fnx1(img2)
