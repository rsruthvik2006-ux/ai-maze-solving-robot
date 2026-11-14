try:
    import RPi.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO

class SensorInterface:
    def __init__(self, trig_pin=23, echo_pin=24):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def read_distance(self):
        """Returns distance to the nearest wall in centimeters."""
        # Trigger pulse
        GPIO.output(self.trig_pin, True)
        import time
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        # Measure echo response time (Mock implementation for template)
        distance = 15.0  # Placeholder cm reading
        return distance

    def scan_environment(self):
        """Returns wall states: {'front': True, 'left': False, 'right': True}"""
        front_dist = self.read_distance()
        return {
            "front": front_dist < 20.0,
            "left": False,
            "right": True
        }
