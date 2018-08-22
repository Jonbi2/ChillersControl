from threading import Thread

import time, sys
import datetime

is_GPIO_recognized = True

try:
    import RPi.GPIO as GPIO
except:
    print("No GPIO pins have been detected, flow_meter")
    is_GPIO_recognized = False


class FlowMeter:

    def __init__(self, pin_connected):
        self.id = 1  # TODO
        self.pin = pin_connected

        # Use GPIO.BOARD - standard mapping
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_connected, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # Used for checking how many falling edges come from the device in a time period
        self.count = 0

        GPIO.add_event_detect(pin_connected, GPIO.FALLING, callback=self.count_pulse)

    def count_pulse(self, callback):
        self.count = self.count + 1

    def start_counting(self):
        self.count = 0
    
    def get_data(self, time_passed):
        # start_counting must be called beforehand and time between the two must be measured and put in here for get_data to work properly
        value = self.count/time_passed/5.5
        result = [{'reading': value, 'sensor_id': self.id}]
        return result

if is_GPIO_recognized:
    flow_meters = [FlowMeter(40)]
else:
    flow_meters = []
