from tokenize import Double
from turtle import width
import matplotlib.image as img
import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb): # RGB2GRAY Matlab format ITU-R
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = np.round(0.299 * r + 0.587 * g + 0.114 * b)
    return gray

def blurMetric(imagePath):

    #Insiasi
    totBM = 0
    totEdges = 0
    leftValue = 0
    rightValue = 0

    image = cv2.imread(imagePath)
    gray = rgb2gray(image)
    img_blur = cv2.GaussianBlur(gray, (3,3), 0)

    # edge detection https://learnopencv.com/edge-detection-using-opencv/
    hEdge = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3, scale=1) #X axis
    vEdge = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3, scale=1) #Y Axis
    hvEdge = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3, scale=1) #Both
    
    row,column,channel = image.shape
    

    #Horizontal blur analysis
    for imCol in range(0,column):
        for imRow in range(0,row):
            if hEdge[imRow][imCol]==1:
                edgePix = img_blur[imRow][imCol]
                leftNbr = img_blur[imRow][imCol-1]
                rightNbr = img_blur[imRow][imCol+1]

                #Tracing Left
                if edgePix > leftNbr:
                    for x in range(imCol-1,-1):
                        if x != 1:
                            if img_blur[imRow][x-1] >= img_blur[imRow][x]:
                                leftValue = x
                                break
                            else:
                                leftValue = img_blur[imRow][x+1]
                        else:
                            leftValue = x+1
                elif edgePix < leftNbr:
                    for x in range(imCol-1,-1):
                        if x != 1:
                            if img_blur[imRow][x-1] <= img_blur[imRow][x]:
                                leftValue = x
                                break
                        else:
                            leftValue = x+1
                elif edgePix == leftNbr:
                    leftValue = imCol
                
                #Tracing Right
                if edgePix > rightNbr:
                    for x in range(imCol+1,column-1):
                        if x != column-1:
                            if img_blur[imRow][x+1] >= img_blur[imRow][x]:
                                rightValue = x
                                break
                            else:
                                rightValue = img_blur[imRow][x-1]
                        else:
                            rightValue=x-1
                elif edgePix < rightNbr:
                    for x in range(imCol+1,column-1):
                        if x != column-1:
                            if img_blur[imRow][x+1]<=img_blur[imRow][x]:
                                rightValue = x
                                break
                        else:
                            rightValue = x-1
                        
                elif edgePix == rightNbr:
                    rightValue = imCol
                
                edgeWidth = float(rightValue) - float(leftValue)
                totBM = totBM + edgeWidth
                totEdges = totEdges + 1

    hBlur = totBM/totEdges
    totBM = 0
    totEdges = 0
    

    # Vertical Blur
    upValue = 0
    downValue = 0
    for imCol in range(0,column):
        for imRow in range(0,row):
            if vEdge[imRow][imCol]==1:
                edgePix = img_blur[imRow][imCol]
                upNbr = img_blur[imRow-1][imCol]
                downNbr = img_blur[imRow+1][imCol]

                #tracing up

                if edgePix > upNbr:
                    for y in range(imRow-1,-1):
                        if y!=1:
                            if img_blur[y-1][imCol] >= img_blur[y][imCol]:
                                upValue = y
                                break
                            else:
                                upValue = img_blur[y+1][imCol]
                        else:
                            upValue = y+1
                elif edgePix < upNbr:
                    for y in range(imRow-1,-1):
                        if y != 1:
                            if img_blur[y-1][imCol] <= img_blur[y][imCol]:
                                upValue = y
                                break
                        else:
                            upValue = y+1
                elif edgePix == upNbr:
                    upValue = imRow

                #Tracking Down
                if edgePix > downNbr:
                    for y in range(imRow+1,row-1):
                        if y != row-1:
                            if img_blur[y+1][imCol] >= img_blur[y][imCol]:
                                downValue = y
                                break
                            else:
                                downValue = img_blur[y-1][imCol]
                        else:
                            downValue = y-1
                elif edgePix < downNbr:
                    for y in range(imRow+1,row-1):
                        if y != row-1:
                            if img_blur[y+1][imCol] <= img_blur[y][imCol]:
                                downValue = y
                                break
                        else:
                            downValue = y-1
                elif edgePix == downNbr:
                    downValue = imRow
                
                edgeWidth = float(downValue)-float(upValue)

                totBM = totBM + edgeWidth
                totEdges = totEdges +1
    vBlur = totBM/totEdges
    totalBlurMetric = (hBlur+vBlur)/2
    totalBlurMetric*=10
    if totalBlurMetric < 0:
        totalBlurMetric = 0
    elif totalBlurMetric > 100:
        totalBlurMetric = 100
    else:
        totalBlurMetric = round(totalBlurMetric)
    return totalBlurMetric



                
        




print(blurMetric("C:/Users/affaa/Downloads/img4.bmp"))