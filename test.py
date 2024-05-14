import time
import numpy as np
import RPi.GPIO as GPIO

enA=2
IN1=3
IN2=4
enB=17
IN1=27
IN2=22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

def motor_forward():
    GPIO.output(enA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(enB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    print("Motor Forward")
    
def motor_reverse():
    GPIO.output(enA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(enB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
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
