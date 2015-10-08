__author__ = 'KolesnikG'

import cv2

img=cv2.imread("1.jpg",0)

def Nibleck_method(img):

    img_size=img.shape[0]*img.shape[1]
    sigma=xa=0

    #Mean
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            xa+=img[i][j]
    xa=xa/img_size

    #Standard diviation
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            sigma+=(img[i][j]-xa)**2
    sigma=(sigma/img_size)**(0.5)


    th=xa-0.2*sigma
    return th

print('threshold = ',round(Nibleck_method(img)))

#ret, thresh=cv2.threshold(img,th,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite("1thN.jpg",thresh)