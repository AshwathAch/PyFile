import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins connected to the L298N motor driver inputs
# Motor A
motorA_enable_pin = 17  # GPIO pin for ENA
motorA_in1_pin = 18      # GPIO pin for IN1
motorA_in2_pin = 27      # GPIO pin for IN2

# Motor B
motorB_enable_pin = 22  # GPIO pin for ENB
motorB_in1_pin = 23      # GPIO pin for IN3
motorB_in2_pin = 24      # GPIO pin for IN4

def setup_gpio():
    # Set up GPIO mode and warnings
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set up motor A pins
    GPIO.setup(motorA_enable_pin, GPIO.OUT)
    GPIO.setup(motorA_in1_pin, GPIO.OUT)
    GPIO.setup(motorA_in2_pin, GPIO.OUT)

    # Set up motor B pins
    GPIO.setup(motorB_enable_pin, GPIO.OUT)
    GPIO.setup(motorB_in1_pin, GPIO.OUT)
    GPIO.setup(motorB_in2_pin, GPIO.OUT)

def motor_a_forward():
    GPIO.output(motorA_in1_pin, GPIO.HIGH)
    GPIO.output(motorA_in2_pin, GPIO.LOW)
    GPIO.output(motorA_enable_pin, GPIO.HIGH)  # Enable motor A

def motor_a_backward():
    GPIO.output(motorA_in1_pin, GPIO.LOW)
    GPIO.output(motorA_in2_pin, GPIO.HIGH)
    GPIO.output(motorA_enable_pin, GPIO.HIGH)  # Enable motor A

def motor_b_forward():
    GPIO.output(motorB_in1_pin, GPIO.HIGH)
    GPIO.output(motorB_in2_pin, GPIO.LOW)
    GPIO.output(motorB_enable_pin, GPIO.HIGH)  # Enable motor B

def motor_b_backward():
    GPIO.output(motorB_in1_pin, GPIO.LOW)
    GPIO.output(motorB_in2_pin, GPIO.HIGH)
    GPIO.output(motorB_enable_pin, GPIO.HIGH)  # Enable motor B

def stop_motors():
    # Disable both motors
    GPIO.output(motorA_enable_pin, GPIO.LOW)
    GPIO.output(motorB_enable_pin, GPIO.LOW)

def cleanup_gpio():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup_gpio()

        # Example: Turn Motor A forward for 3 seconds
        print("Turning Motor A forward...")
        motor_a_forward()
        sleep(3)  # Motor A runs for 3 seconds
        stop_motors()

        # Example: Turn Motor B backward for 2 seconds
        print("Turning Motor B backward...")
        motor_b_backward()
        sleep(2)  # Motor B runs for 2 seconds
        stop_motors()

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        cleanup_gpio()
