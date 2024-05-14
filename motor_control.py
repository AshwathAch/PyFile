import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor control pins
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Set up GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to control motors
def move_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def move_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop_motors():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Main program
try:
    while True:
        move_forward()  # Move motors forward
        time.sleep(2)   # Run motors for 2 seconds
        stop_motors()   # Stop motors
        time.sleep(1)   # Pause for 1 second
        move_backward() # Move motors backward
        time.sleep(2)   # Run motors backward for 2 seconds
        stop_motors()   # Stop motors
        time.sleep(1)   # Pause for 1 second

except KeyboardInterrupt:
    stop_motors()     # Stop motors on keyboard interrupt
    GPIO.cleanup()    # Clean up GPIO on exit
