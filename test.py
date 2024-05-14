import cv2, os, sys, pickle
import time
import numpy as np
import RPi.GPIO as GPIO
import serial
ser1 = serial.Serial('/dev/ttyUSB0',9600,timeout=0.5)
motor_relay1=2
motor_relay2=3
motor_relay3=4
motor_relay4=17


full_relay1=27
full_relay2=22

center_relay1=10
center_relay2=9

height_relay1=19
height_relay2=26



limit1=21
limit2=20

limit3=6
limit4=13

limit5=23

CAMERA1=11
CAMERA2=0



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CAMERA1,  GPIO.OUT)
GPIO.setup(CAMERA2,  GPIO.OUT)

GPIO.setup(motor_relay1, GPIO.OUT)
GPIO.setup(motor_relay2, GPIO.OUT)
GPIO.setup(motor_relay3, GPIO.OUT)
GPIO.setup(motor_relay4, GPIO.OUT)

GPIO.setup(full_relay1,  GPIO.OUT)
GPIO.setup(full_relay2,  GPIO.OUT)

GPIO.setup(center_relay1, GPIO.OUT)
GPIO.setup(center_relay2, GPIO.OUT)

GPIO.setup(height_relay1, GPIO.OUT)
GPIO.setup(height_relay2, GPIO.OUT)


GPIO.output(CAMERA1, False)
GPIO.output(CAMERA2, False)

GPIO.output(motor_relay1, False)
GPIO.output(motor_relay2, False)
GPIO.output(motor_relay3, False)
GPIO.output(motor_relay4, False)


GPIO.output(center_relay1, False)
GPIO.output(center_relay2, False)

GPIO.output(height_relay1, False)
GPIO.output(height_relay2, False)


GPIO.output(full_relay1, False)
GPIO.output(full_relay2, False)

GPIO.setup(limit1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limit2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limit3, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limit4, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limit5, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def motor_forward():
    
    GPIO.output(motor_relay1, False)
    GPIO.output(motor_relay2, True)
    GPIO.output(motor_relay3, False)
    GPIO.output(motor_relay4, True)
    print("dMOtor Forward")
def motor_reverse():
    
    GPIO.output(motor_relay1, True)
    GPIO.output(motor_relay2, False)
    GPIO.output(motor_relay3, True)
    GPIO.output(motor_relay4, False)
    print("Motor Reverse")
def motor_left():
    
    GPIO.output(motor_relay1, False)
    GPIO.output(motor_relay2, True)
    GPIO.output(motor_relay3, True)
    GPIO.output(motor_relay4, False)
    print("Motor Left")
def motor_right():
    
    GPIO.output(motor_relay1, True)
    GPIO.output(motor_relay2, False)
    GPIO.output(motor_relay3, False)
    GPIO.output(motor_relay4, True)
    print("Motor Right")
def motor_stop():
    GPIO.output(motor_relay1, False)
    GPIO.output(motor_relay2, False)
    GPIO.output(motor_relay3, False)
    GPIO.output(motor_relay4, False)
    print("Motor Stop")
def center_foward():
    GPIO.output(center_relay1, False)
    GPIO.output(center_relay2, True)
    print("Center forward")
def center_reverse():
    GPIO.output(center_relay1, True)
    GPIO.output(center_relay2, False)
    print("Center reverse")
def center_stop():
    GPIO.output(center_relay1, False)
    GPIO.output(center_relay2, False)
    print("Center Stop")
def full_forward():
    GPIO.output(full_relay1, True)
    GPIO.output(full_relay2, False)
    print("Full forward")
def full_reverse():
    GPIO.output(full_relay1, False)
    GPIO.output(full_relay2, True)
    print("Full Reverse")
def full_stop():
    GPIO.output(full_relay1, False)
    GPIO.output(full_relay2, False)   
    print("FullStop")
def height_forward():
    GPIO.output(height_relay1, True)
    GPIO.output(height_relay2, False)
    print("Height Forward")
def height_reverse():
    GPIO.output(height_relay1, False)
    GPIO.output(height_relay2, True)
    print("Height Reverse")
def height_stop():
    GPIO.output(height_relay1, False)
    GPIO.output(height_relay2, False)
    print("height stop")
#center_reverse()
#height_forward()
def camera():
     GPIO.output(CAMERA1, True)
     GPIO.output(CAMERA2, False)
     time.sleep(2)
     GPIO.output(CAMERA1, False)
     GPIO.output(CAMERA2, False)
     print("Camera rotate")
def clamp():
    
    #while(GPIO.input(limit2)==0):
    print("clip motor")
    height_forward()
    time.sleep(10)
    height_stop()
    print("clamp")
    
def unclamp():
    print("hhhh")
    height_reverse()
    time.sleep(10)
    height_stop()
    print("unclamp")
    
def down():
    
    #while(GPIO.input(limit1)==0):
    
    print("downing")
    full_reverse()
    time.sleep(60)
    
    full_stop()
def up():
    #while(GPIO.input(limit3)==0):
    print("uping")
    full_forward()
    time.sleep(70)
    
    full_stop()
def center_right():
     #while(GPIO.input(limit4)==0):
      center_reverse()
      time.sleep(6)
      print("center reverse")
      center_stop()
def center_left():
    #while(GPIO.input(limit5)==0):
    center_foward()
    time.sleep(6)
    print("center forward")
    center_stop()
     
    
def read_ser1():
    s=ser1.readline()
    print(s)
    if s==b'a':
        motor_forward()
    if s==b'b':
        motor_reverse()
    if s==b'c':
        motor_left()
    if s==b'd':
       motor_right()
    if s==b'e':
        motor_stop()
    if s==b'F':  
        object()

classNames = []
classFile = "pt.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")



configPath = "ss.pbtxt"
weightsPath = "ll.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=[]):
    global d
    global count ,m
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    print(className)
                    if className=="cell phone" or "sports ball" or "apple"or"banana" and m==0:
                        
                        down()
                        time.sleep(2)
                        clamp()
                        time.sleep(2)
                        up()
                        time.sleep(2)
                        center_left()
                        time.sleep(2)
                        unclamp()
                        time.sleep(2)
                        center_right()
                        time.sleep(2)
                       
                        
                        
                    
    return img,objectInfo
def object():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        
        success, img = cap.read()
        result, objectInfo = getObjects(img,0.45,0.2,objects=['cell phone','sports ball','apple','banana'])
        #print(objectInfo)
        cv2.imshow("Output",img)
        cv2.waitKey(1)
def main():
   
   
    """down()
    time.sleep(2)
    clamp()
    time.sleep(2)
    up()
    time.sleep(2)
    center_left()
    time.sleep(2)
    unclamp()
    time.sleep(2)
    center_right()
    time.sleep(2)
    """                  
    while True:
        
        
       read_ser1()
        
        
main()
