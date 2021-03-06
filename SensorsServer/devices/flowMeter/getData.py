from threading import Thread

import time, sys
import datetime
import json

is_GPIO_recognized = True

try:
    import RPi.GPIO as GPIO
except Exception as exception:
    print(exception)
    print("No GPIO pins have been detected, flow_meter")
    is_GPIO_recognized = False


class FlowMeter:
    def __init__(self, pin_connected, correction_ratio):
        self.id = pin_connected
        self.correction_ratio = correction_ratio

        # Use GPIO.BOARD - standard mapping
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_connected, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # Used for checking how many falling edges come from the device in a time period
        self.count = 0

        GPIO.add_event_detect(pin_connected, GPIO.FALLING, callback=self.count_pulse)

    def count_pulse(self):
        self.count = self.count + 1

    def start_counting(self):
        self.count = 0
    
    def get_data(self, time_passed):
        # start_counting must be called beforehand and time between the two must be measured and put in here for get_data to work properly
        value = self.count/time_passed/self.correction_ratio
        result = [{'reading': value, 'sensor_id': self.id}]
        return result

if is_GPIO_recognized:
    json_flow_meter_data = json.load(open('config.json'))['FlowMeters']
    flow_meters_number = len(json_flow_meter_data)
    flow_meters = []
    for i in range(0, flow_meters_number):
        pin = json_flow_meter_data[i]["Pin"]
        correction_ratio = json_flow_meter_data[i]["CorrectionRatio"]
        sensor_id = i
        flow_meters.append(FlowMeter(pin, correction_ratio))
else:
    flow_meters = []
