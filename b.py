from ast import Constant
from time import sleep
import numpy as np
#import cv2
#import numpy as np
#from PIL import Image
#import pygetwindow
import pyautogui

import torch
import cv2
import numpy as np


# Model

model = torch.hub.load('ultralytics/yolov5','yolov5s',pretrained=True)

# Image
#im = 'videoplayback.mp4'
#for image

def calc(im):
    c = [0]*6
    #c[5]=0
    #im=cv2.imread(n1)
    im = cv2.cvtColor(np.array(im),cv2.COLOR_RGB2BGR)
        # Inference
    results = model(im)


    #1-bicycle
    #2.-cars
    #3-motorcycle
    #5-bus
    #7-truck
    for box in results.xyxy[0]: 
                    if box[5]==1:
                        c[0]+=1
                    elif box[5]==2:
                        c[1]+=1
                    elif box[5]==3:
                        c[2]+=1
                    elif box[5]==5:
                        c[3]+=1
                    elif box[5]==7:
                        c[4]+=1
                    
                        #xB = int(box[2])
                        #xA = int(box[0])
                        #yB = int(box[3])
                        #yA = int(box[1])
                        #cv2.rectangle(im, (xA, yA), (xB, yB), (0, 255, 0), 2)
                        #cv2.imshow('Example - Show image in window',im)

    #print(cars) 
    #cv2.imshow('Example - Show image in window',im)
    #cv2.waitKey(0) # waits until a key is pressed
    #cv2.destroyAllWindows()   '
    c[5]=((c[0]*2)+(c[1]*3)+(c[2]*2.5)+(c[3]*2.5)+(c[4]*3.5))/2 

    if (c[5]>60):
        c[5]=60
    elif (c[5]<5):
        c[5]=5    
    #print(c[5])
    return c
def send(x,y,h,w):
    #titles=pygetwindow.getAllTitles()
    #print(titles)
    #x1,y1,w,h=pygetwindow.getWindowGeometry('player')
    ##x2=x1+w
    #y2=y1+h
    i1=pyautogui.screenshot(region=(x,y,h,w))
    #i1=i1.crop((100,100,1000,1000))
    #i1.show()
    c1=calc(i1)
    #c1=int(c.calc(i1))
    #img=np.array(Image.grab(bbox=(0,0,800,600)))
    #cv2.imshow('Python Window', i1)
    #c1=int(c.my_fun(img))
    #print(c1)
    #c1=1
    return c1






    
    


"""
def send():
    #c1=int(c.my_fun('1.jpg'))
    img=np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    cv2.imshow('Python Window', img)
    #c1=int(c.my_fun('1.jpg'))
    #print(c1)
    c1=1
    return c1*100
"""
