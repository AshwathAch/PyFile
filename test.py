from gpiozero import Motor, OutputDevice
from time import sleep

# Define motor objects
motor_a = Motor(forward=17, backward=18)  # GPIO pins for Motor A (IN1, IN2)
motor_b = Motor(forward=22, backward=23)  # GPIO pins for Motor B (IN3, IN4)

# Example: Move Motor A forward for 3 seconds
motor_a.forward()
sleep(3)
motor_a.stop()

# Example: Move Motor B backward for 2 seconds
motor_b.backward()
sleep(2)
motor_b.stop()
