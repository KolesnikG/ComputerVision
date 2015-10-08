__author__ = 'KolesnikG'

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import binarization_methods as method


img=cv2.imread("1.jpg",0)
img1=cv2.imread("2.jpg",0)

def calculate_histogram(img):
    hist_data=[0]*256
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            hist_data[img[i][j]]+=1;
    return hist_data


def build_histogram(hist_data,th1,th2,th3,s):
    k=np.arange(0,256)
    hist, bins = np.histogram(k, bins=256)
    width = 2 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2


    fig = plt.figure()

    plt.bar(center, hist_data, width=width)

    plt.bar(th1,s,1.5,color='c')
    plt.bar(th2,s,1,color='r')
    plt.bar(th3,s,1,color='y')

th1=method.gradient_method(img)
th2=method.Otsu_method(img)
th3=method.Nibleck_method(img)

print(th1,th2,th3)

ret,thresh1=cv2.threshold(img,th1,255,cv2.THRESH_BINARY_INV)
ret,thresh2=cv2.threshold(img,th2,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,th3,255,cv2.THRESH_BINARY_INV)

cv2.imwrite('grad.jpg',thresh1)
cv2.imwrite('otsu.jpg',thresh2)
cv2.imwrite('nibleck.jpg',thresh3)


build_histogram(calculate_histogram(img),th1,th2,th3,s=3500)

blue_line = mlines.Line2D([], [], color='c', label='Gradient threshold')
blue_line1 = mlines.Line2D([], [], color='r', label='Otsu threshold')
blue_line2 = mlines.Line2D([], [], color='y', label='Nibleck threshold')
plt.legend(handles=[blue_line,blue_line1,blue_line2],loc=2)

build_histogram(calculate_histogram(img1),th1,th2,th3,s=35)

blue_line = mlines.Line2D([], [], color='c', label='Gradient threshold')
blue_line1 = mlines.Line2D([], [], color='r', label='Otsu threshold')
blue_line2 = mlines.Line2D([], [], color='y', label='Nibleck threshold')


plt.legend(handles=[blue_line,blue_line1,blue_line2],loc=1)

plt.show()