__author__ = 'KolesnikG'

import numpy as np
a={}
a=[[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,0,0], [0,0,0,0,1,1,1,1,0,0,0,0],
   [0,0,1,1,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,0,0], [0,0,0,0,1,1,1,1,1,1,0,0],
   [0,0,1,1,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,0,0], [0,0,0,0,1,1,1,1,1,1,0,0],
   [0,0,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]]


def print_img(img):
    for i in range(0,12):
        for j in range(0,12):
            print(img[i][j],end='\t')
        print(' ')

neighbors = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
print_img(a)
d=[[] for i in range(2)]

def contour_obj(a):
    boundary_point=[(1,4)]
    i,j=boundary_point[0]
    si,sj=i,j
    a[i][j]=2
    k=0
    m,n=neighbors[0]
    while k<8:
            m,n=neighbors[k]
            if (a[i+m][j+n]!=1) and (a[i+m][j+n]!=2):
                if k==7:
                    k=0
                else:
                    k+=1
            else:
                j,i=j+n,i+m
                d[0]+=[(i,j)]
                a[i][j]=2
                k-=1
                if i==si and j==sj:
                    break
                #print_img(a)
                #print(' ')
    return d



d=contour_obj(a)
def fit_contour(d):
    coord=[[0,0,0,0] for i in range(len(d)-1)]
    k=0;
    while(k<len(d)-1):
        l1=[];l2=[]
        for i in range(0,len(d[k])):
            l1+=[d[k][i][0]]
            l2+=[d[k][i][1]]
        coord[k]=np.amin(l1),np.amin(l2),np.amax(l1),np.amax(l2)
        k+=1
    return coord

print(fit_contour(d))

