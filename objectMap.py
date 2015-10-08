__author__ = 'KolesnikG'

import cv2
import numpy as np


img=cv2.imread("otsu1.jpg",0)

ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cur=1;
def numerated(img):
    global cur
    km=kn=0
    for i in range(1,img.shape[0]):
        for j in range(1,img.shape[1]):
            kn = j - 1
            if kn <= 0:
                kn = 1
                B = 0
            else:
                B = img[i][kn]
            km = i - 1
            if km <= 0:
                km = 1
                C = 0
            else:
                C = img[km][j]

            A = img[i][j]
            if A==0: pass
            elif (B==0 and C==0):
                cur+=1
                img[i][j] = cur
            elif (B != 0 and C==0):
                img[i][j]=B
            elif (B==0 and C!=0):
                img[i][j]=C
            elif (B!=0 and C!=0):
                if B==C:
                    img[i][j]=B
                else:
                    img[i][j]=B
                    img[img==C]=B
    return img

img=numerated(img)

def filter(img, bigvalue):
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if img[i][j] not in bigvalue:
                img[i][j]=0
    return img


def print_img(img):
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            print(img[i][j],end='\t')
        print(' ')


def get_bigvalue(img,cur):
    m=[0]*(cur+1);bigvalue=[]
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            m[img[i][j]]+=1
    for i in range(1,len(m)):
        if m[i]>700:
            bigvalue+=[i]
    return bigvalue

bigv=get_bigvalue(img,cur)
contour=[[] for i in range(len(bigv))]

img=filter(img,bigv)


neighbors = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def find_boundary(img,bigv):
    boundary_coord=[];k=0;
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if img[i][j]==bigv[k]:
                boundary_coord+=[(i,j)]
                k+=1
                if k>=len(bigv):
                    return boundary_coord

#bound_point=find_boundary(img,bigv)

def contour_obj(boundary_point):
    i,j=boundary_point[0]
    si,sj=i,j
    img[i][j]=1
    k=0
    while k<8:
            m,n=neighbors[k]
            if (img[i+m][j+n]!=1) and (img[i+m][j+n]!=bigv[0]):
                if k==7:
                    k=0
                else:
                    k+=1
            else:
                j,i=j+n,i+m
                contour[0]+=[(i,j)]
                img[i][j]=1
                k-=1
                if i==si and j==sj:
                    break


#img=contour_obj(bound_point)


print_img(img)