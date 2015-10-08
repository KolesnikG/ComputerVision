__author__ = 'KolesnikG'

import cv2
import numpy as np

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
    return round(th)

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
    return round(th)

def Otsu_method(img):

    sum_all=sum_back=w_back=w_for=var_max=threshold=0
    hist_data=[0]*256
    img_size=img.shape[0]*img.shape[1]

    #histogram
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            hist_data[img[i][j]]+=1;


    for t in range(256):
        sum_all+=t*hist_data[t]

    for t in range(256):
        w_back+=hist_data[t]
        if w_back==0:continue
        w_fore=img_size-w_back
        if w_fore==0:break

        sum_back += t*hist_data[t]
        mean_back = sum_back / w_back
        mean_fore = (sum_all - sum_back) / w_fore

        var_between = w_back * w_fore * (mean_back - mean_fore)**2

        if (var_between > var_max):
            var_max = var_between
            th = t
    return round(th)


