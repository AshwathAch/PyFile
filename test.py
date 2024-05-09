import RPi.GPIO as GPIO
import time

# Define GPIO pins connected to the relay modules
motor_relay1 = 2
motor_relay2 = 3
motor_relay3 = 4
motor_relay4 = 17

# Setup GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup GPIO pins for motor control (output)
GPIO.setup(motor_relay1, GPIO.OUT)
GPIO.setup(motor_relay2, GPIO.OUT)
GPIO.setup(motor_relay3, GPIO.OUT)
GPIO.setup(motor_relay4, GPIO.OUT)

def motor_forward():
    GPIO.output(motor_relay1, GPIO.LOW)
    GPIO.output(motor_relay2, GPIO.HIGH)
    GPIO.output(motor_relay3, GPIO.LOW)
    GPIO.output(motor_relay4, GPIO.HIGH)
    print("Motor Forward")

def motor_reverse():
    GPIO.output(motor_relay1, GPIO.HIGH)
    GPIO.output(motor_relay2, GPIO.LOW)
    GPIO.output(motor_relay3, GPIO.HIGH)
    GPIO.output(motor_relay4, GPIO.LOW)
    print("Motor Reverse")

def motor_left():
    GPIO.output(motor_relay1, GPIO.LOW)
    GPIO.output(motor_relay2, GPIO.HIGH)
    GPIO.output(motor_relay3, GPIO.HIGH)
    GPIO.output(motor_relay4, GPIO.LOW)
    print("Motor Left")

def motor_right():
    GPIO.output(motor_relay1, GPIO.HIGH)
    GPIO.output(motor_relay2, GPIO.LOW)
    GPIO.output(motor_relay3, GPIO.LOW)
    GPIO.output(motor_relay4, GPIO.HIGH)
    print("Motor Right")

def motor_stop():
    GPIO.output(motor_relay1, GPIO.LOW)
    GPIO.output(motor_relay2, GPIO.LOW)
    GPIO.output(motor_relay3, GPIO.LOW)
    GPIO.output(motor_relay4, GPIO.LOW)
    print("Motor Stop")

try:
    # Example usage:
    motor_forward()
    time.sleep(2)  # Motor runs forward for 2 seconds
    motor_stop()
    time.sleep(1)

    motor_reverse()
    time.sleep(2)  # Motor runs reverse for 2 seconds
    motor_stop()
    time.sleep(1)

    motor_left()
    time.sleep(2)  # Motor turns left for 2 seconds
    motor_stop()
    time.sleep(1)

    motor_right()
    time.sleep(2)  # Motor turns right for 2 seconds
    motor_stop()

except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    GPIO.cleanup()  # Clean up GPIO pins on program exit
