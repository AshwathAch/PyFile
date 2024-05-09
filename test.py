import RPi.GPIO as GPIO
import time

# Define GPIO pins connected to the L298N motor driver inputs
ENA = 17  # GPIO pin for ENA
IN1 = 22  # GPIO pin for IN1
IN2 = 23  # GPIO pin for IN2
ENB = 18  # GPIO pin for ENB
IN3 = 24  # GPIO pin for IN3
IN4 = 25  # GPIO pin for IN4

# Setup GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup GPIO pins for motor control (output)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)  # Enable Motor A
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENB, GPIO.HIGH)  # Enable Motor B
    print("Motors Forward")

def motor_reverse():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(ENA, GPIO.HIGH)  # Enable Motor A
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)  # Enable Motor B
    print("Motors Reverse")

def motor_stop():
    GPIO.output(ENA, GPIO.LOW)  # Disable Motor A
    GPIO.output(ENB, GPIO.LOW)  # Disable Motor B
    print("Motors Stopped")

try:
    motor_forward()
    time.sleep(2)  # Motors run forward for 2 seconds
    motor_stop()
    time.sleep(1)

    motor_reverse()
    time.sleep(2)  # Motors run reverse for 2 seconds
    motor_stop()
    time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    GPIO.cleanup()  # Clean up GPIO pins on program exit
