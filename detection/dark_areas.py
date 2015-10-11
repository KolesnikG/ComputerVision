__author__ = 'KolesnikG'
import numpy as np
import cv2

name=str(input('Enter the file name: '))
img = cv2.imread(name)
index=name.find('.jpg')
name=name[:index]+'(binRes)'+'.jpg'


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#equ=cv2.equalizeHist(gray)
#gray = np.hstack((gray,equ))
#cv2.imwrite("s.jpg", gray)

#clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(470,470))
#gray = clahe.apply(equ)

gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
#thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
ret, thresh = cv2.threshold(gray_blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel, iterations=1)
cont_img=closing.copy()
image, contours, hierarchy = cv2.findContours(cont_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('All contours:',len(contours))


def getCount(cnt):
    count=[]
    for c in contours:
            area = cv2.contourArea(c)
            if area < 700 or area > 1000000:
                continue
            else:
                count+=[c]
    return count
print('After calibration:',len(getCount(contours)))

def getMask(cnt, i):
    mask = np.zeros_like(thresh)
    cv2.drawContours(mask, cnt,i, 255, -1)
    out = np.zeros_like(thresh)
    out[mask == 255] = thresh[mask == 255]
    return out

def getContourImage(cnt,i):
    box=np.int0(cv2.boxPoints(cv2.minAreaRect(cnt[i])))
    x=box[0][0];y=box[1][1]
    w=box[3][0];h=box[0][1]

    z=getMask(cnt,i)[y:h,x:w]

    if z.size==0:
        return False
    elif cv2.countNonZero(z)/z.size<0.2:
        return False
    else:
        print('Rectangle','x:',x,', y:',y,', w:',w,', h:',h)
        return True

c=getCount(contours)
for i in range(0,len(c)):
    if  getContourImage(c,i)==True:
        ell = cv2.fitEllipse(c[i])
        cv2.ellipse(img, ell, (0,255,0), 2)
        box=np.int0(cv2.boxPoints(cv2.minAreaRect(c[i])))
        cv2.drawContours(img,[box],0,(0,0,255),1)

cv2.imwrite(name,img)
print('Image was saved in program folder(dest) with name:',name)
