import time
from time import sleep

import json


is_GPIO_recognized = True

# freely chosen SPI pins
SPICLK = 36  # BOARD 36
SPIMISO = 35  # BOARD 35
SPIMOSI = 38  # BOARD 38
SPICS = 22  # BOARD 22

try:
    import RPi.GPIO as GPIO
# set up the SPI interface pins
    GPIO.setup([SPIMOSI, SPICLK, SPICS], GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
except Exception as exception:
    print(exception)
    print("No GPIO pins have been detected, QBE2002_P25")
    is_GPIO_recognized = False

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout


class QBE2002P25PressureSensor:
    def __init__(self, adc_pin, pressure_range):
        self.adc_pin = adc_pin
        self.pressure_range = pressure_range

    def get_qbe2002_p25_data(self):
        digital_reading = readadc(self.adc_pin, SPICLK,
                           SPIMOSI, SPIMISO, SPICS)
        pressure = digital_reading * self.pressure_range / 1024.0
        if self.pressure_range is 40:
            pressure = pressure + 0.35
        result = {'reading': pressure, 'sensor_id': self.adc_pin}
        return result


if is_GPIO_recognized:
    json_pressure_sensors_data = json.load(open('config.json'))['PressureSensors']
    pressure_sensors_number = len(json_pressure_sensors_data)
    pressure_sensors = []
    for i in range(0, pressure_sensors_number):
        sensor_pin = json_pressure_sensors_data[i]["SensorMCP3008Pin"]
        sensor_range = json_pressure_sensors_data[i]["MeasurmentRange"]
        pressure_sensors.append(QBE2002P25PressureSensor(sensor_pin, sensor_range))
else:
    pressure_sensors = []
