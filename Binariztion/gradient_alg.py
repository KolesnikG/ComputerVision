__author__ = 'KolesnikG'

import cv2
import numpy as np

img=cv2.imread("1.jpg",0)


def gradient_method(img):
    Gm=Gn=np.zeros_like(img)

    for m in range(1,img.shape[0]-1):
        for n in range(1,img.shape[1]-1):
            Gm[m][n]=(int(img[m+1][n])-int(img[m-1][n]))/2
            Gn[m][n]=(int(img[m][n+1])-int(img[m][n-1]))/2

    G=np.maximum(Gm,Gn)
    part1=part2=0

    for m in range(0,img.shape[0]):
        for n in range(0,img.shape[1]):
            part1+=int(img[m][n])*int(G[m][n])
            part2+=int(G[m][n])

    th=part1/part2
    return th


print('threshold = ',round(gradient_method(img)))
#ret,thresh=cv2.threshold(img,th,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite("grad1.jpg",thresh)