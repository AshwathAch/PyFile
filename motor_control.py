import RPi.GPIO as GPIO
from time import sleep

# GPIO pins connected to motor driver
forward_pin = 17
reverse_pin = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(reverse_pin, GPIO.OUT)

def forward():
    GPIO.output(forward_pin, GPIO.HIGH)
    GPIO.output(reverse_pin, GPIO.LOW)
    print("Motor moving forward")
    # Add any other motor control logic here
    sleep(5)  # Motor runs for 5 seconds
    GPIO.output(forward_pin, GPIO.LOW)

def reverse():
    GPIO.output(forward_pin, GPIO.LOW)
    GPIO.output(reverse_pin, GPIO.HIGH)
    print("Motor moving reverse")
    # Add any other motor control logic here
    sleep(5)  # Motor runs for 5 seconds
    GPIO.output(reverse_pin, GPIO.LOW)

# Clean up GPIO on exit
def cleanup_gpio():
    GPIO.cleanup()

# Call cleanup function on exit
import atexit
atexit.register(cleanup_gpio)
