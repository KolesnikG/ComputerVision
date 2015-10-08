__author__ = 'KolesnikG'

import cv2

img=cv2.imread("1.jpg",0)


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
    return th

print('threshold = ',round(Otsu_method(img)))