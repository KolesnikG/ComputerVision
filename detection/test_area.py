__author__ = 'Администратор'
import numpy as np
import cv2
from matplotlib import pyplot as plt
from math import *
import PIL.Image as im

img = cv2.imread('r1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
#thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
ret, thresh = cv2.threshold(gray_blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel, iterations=1)
cont_img=closing.copy()
image,contours, hierarchy = cv2.findContours(cont_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))

def getCount(cnt):
    count=[]
    for c in contours:
            area = cv2.contourArea(c)
            if area < 400 or area > 100000:
                continue
            else:
                count+=[c]
    return count
print(len(getCount(contours)))

c=getCount(contours)
i=-1
ell = cv2.fitEllipse(c[0])
cv2.ellipse(img, ell, (0,255,0), 2)

for i in range(0,len(getCount(contours))):
    i=i+1
    mask = np.zeros_like(thresh)
    cv2.drawContours(mask,c,i, 255, -1)
    out = np.zeros_like(thresh)
    out[mask == 255] = thresh[mask == 255]
    cv2.imwrite("res.jpg", out)


#cv2.imwrite("res.jpg", img)