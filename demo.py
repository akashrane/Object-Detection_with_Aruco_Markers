import cv2
import numpy as np
from demodetector import *


parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

detection = HomogeneousBgDetector()

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _, img = capture.read()
    corners, _, _ = cv2.aruco.detectMarkers(img,aruco_dict,parameters=parameters)
    if corners:
        int_cornersvalues  =  np.int0(corners)
        cv2.polylines(img,int_cornersvalues,True,(255,0,0),4)

        arucodigramperimeter = cv2.arcLength(corners[0],True)
        print(arucodigramperimeter)

        pixel_ratio = arucodigramperimeter / 20
        print(pixel_ratio)


        values = detection.detect_objects(img)
        for fmm in values:


            rect = cv2.minAreaRect(fmm)

            (x, y), (w, h), angle = cv2.minAreaRect(fmm)
            (x,y), (w,h), angle = rect

            objectHeight = h / pixel_ratio
            objectWidth = w / pixel_ratio

            box = cv2.boxPoints(rect)
            box=np.int0(box)

            cv2.circle(img, (int(x), int(y)), 3, (0, 255, 255), -1)
            cv2.polylines(img, [box], True, (0, 255, 255), 2)
            cv2.putText(img,"Width {} cm".format(round(objectWidth,1)),(int(x),int(y- 15)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
            cv2.putText(img,"Height {} cm".format(round(objectHeight,1)),(int(x),int(y+ 15)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)




    cv2.imshow("akashwindow",img)
    key = cv2.waitKey(1)
    if key == 113 :
        break

capture.release()
cv2.destroyAllWindows()



