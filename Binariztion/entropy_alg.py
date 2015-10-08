__author__ = 'Kolesnikg'

import cv2,math

img=cv2.imread("1.jpg",0)


def calculate_histogram(img):
    hist_data=[0]*256
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            hist_data[img[i][j]]+=1;
    return hist_data

img_size=img.shape[1]*img.shape[0]
h=calculate_histogram(img)


H=Hs=ps=pq=0
s=134
for i in range(len(h)):
    h[i]/=img_size
for i in range(0,s):
    ps+=h[i]
for i in range(0,s):
    if h[i]==0:continue
    pq+=h[i]*math.log(h[i])
for i in range(len(h)):
    if h[i]==0:continue
    Hs+=h[i]*math.log(h[i])

p=math.log(s*(256-s))

k=pq/(ps*Hs)

print(k)