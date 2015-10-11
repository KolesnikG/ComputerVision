__author__ = 'Администратор'
import numpy as np
import cv2

cap = cv2.VideoCapture(1)
while(cv2.waitKey(1)!=ord('q')):
    ret, frame = cap.read()
    roi = frame[0:500, 0:500]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    ret, thresh = cv2.threshold(gray_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel, iterations=3)

    cont_img = closing.copy()
    image, contours, hierarchy = cv2.findContours(cont_img,1,2)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 2000 or area > 4000:
            continue

        if len(cnt) < 5:
            continue

        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(frame, ellipse, (0,255,0), 2)
    #cv2.imshow("Morphological Closing", closing)
    cv2.imshow("Adaptive Thresholding", thresh)
    #cv2.imshow('Contours', roi)
