import cv2
import numpy as np
import math

def calculateDistance(x1,y1,x2,y2):
      dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
      return dist

def ROI_mask(image):
    
    height = image.shape[0]
    width = image.shape[1]

    
    # A triangular polygon to segment the area and discarded other irrelevant parts in the image
    # Defined by three (x, y) coordinates    
    polygons = np.array([ 
        [(0, height), (round(width/2), round(height/2)), (1000, height)] 
        ]) 
    
    mask = np.zeros_like(image) 
    cv2.fillPoly(mask, polygons, 255)  ## 255 is the mask color
    
    # Bitwise AND between canny image and mask image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image



def SafetyLineCross(frame):
    while True:
        #Gaussian Blur operation the image 
        imag1 = cv2.GaussianBlur(frame, (5, 5), 0)

        #hsv color detection..
        hsv = cv2.cvtColor(imag1, cv2.COLOR_BGR2HSV)

        ly = np.array([18, 94, 140])
        uy = np.array([48, 255, 255])
        mask = cv2.inRange(hsv, ly, uy)
        edges = cv2.Canny(mask, 75, 150)
        cropedImage = ROI_mask(edges)
        #use the hough transform method and the detection is done.
        lines = cv2.HoughLinesP(cropedImage, 1, np.pi/180, 50, maxLineGap=50)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(imag1, (x1, y1), (x2, y2), (0, 255, 0), 5)
                slope=((y2-y1)/(x2-x1))

                m=calculateDistance(x1, y1, x2, y2)
            dist=(slope-3)
              # warning Alert
            if dist <=-0.6:
                cv2.putText(imag1, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)     
            #print("m=",m)
        return imag1