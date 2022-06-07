# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:02:23 2022

@author: xl.li
"""
'''简单的canny检测
import cv2 as cv
ori_img = cv.imread("C:\\Users\\xl.li\\Desktop\\D.png")
img1 = cv.GaussianBlur(ori_img,(3,3),0)
canny = cv.Canny(img1,50,150)
cv.imshow("ori_img",ori_img)
cv.imshow('Canny',canny)
cv.waitKey(0)
cv.destroyAllWindows()
'''
import cv2
#可调节的阈值大小的程序
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3
 
img = cv2.imread("C:\\Users\\xl.li\\Desktop\\D.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
cv2.namedWindow('canny demo')
 
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
 
CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
