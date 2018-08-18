import time
from time import sleep
 
import RPi.GPIO as GPIO

 
# freely chosen SPI pins
SPICLK = 36  # BOARD 36
SPIMISO = 35  # BOARD 35
SPIMOSI = 38  # BOARD 38
SPICS = 22  # BOARD 22
 
# set up the SPI interface pins
GPIO.setup([SPIMOSI, SPICLK, SPICS], GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)

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
    def __init__(self, adc_pin):
        self.potentiometer_adc = adc_pin


    def read_potentiometer(self):
        trim_pot = readadc(self.potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        return round(trim_pot / 1024.0, 2)

    
    def get_qbe2002_p25_data(self):
        trim_pot = readadc(self.potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        result = {'reading': trim_pot * 25.0 / 1024.0, 'sensor_id': 1}
        return result


pressure_sensors = [QBE2002P25PressureSensor(0)]