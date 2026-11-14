try:
    import RPi.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO

class MotorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        # Setup motor driver GPIO pins here

    def move_forward(self):
        print("Robot moving forward...")

    def turn_left(self):
        print("Robot turning left 90 degrees...")

    def turn_right(self):
        print("Robot turning right 90 degrees...")

    def stop(self):
        print("Robot stopped.")

    def cleanup(self):
        GPIO.cleanup()
