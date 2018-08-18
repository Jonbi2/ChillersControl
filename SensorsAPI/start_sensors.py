import time
import termcolor

from tqdm import tqdm

from devices.microDpm680.getCurrentsAndVoltages import get_micro_dpm68_voltages_and_currents_data
from devices.microDpm680.getPowers import get_micro_dpm680_powers_data

from devices.DS18B20.getData import get_ds18b20_data
from devices.flowMeter.getData import flow_meters
from devices.QBE2002_P25.get_data import pressure_sensors

from SqlModeling.microDpm680DatabaseClient import microDpm680_voltage_and_currents_DbClient, microDpm680_powers_DbClient
from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

def start_measurments():
    while True: 
        # Micro Dmp680 handling
        microDpm680_voltage_and_currents_DbClient.push_data(get_micro_dpm68_voltages_and_currents_data())
        # microDpm680_powers_DbClient.push_data(get_micro_dpm680_powers_data())

        # DS18B20 temperatire sensors handling 
        try:
            ds18b20_DbClient.push_data(get_ds18b20_data())
        except RuntimeError as error:
            print(error)
            time.sleep(1)
            start_measurments()

        # Flow meters handling start counting impulses
        flow_meters_counting_start_time = time.time()
        for flow_meter in flow_meters:
            flow_meter.start_counting()

        # QBE Pressure Sensor handling
        for pressure_sensor in pressure_sensors:
            qbe2002p25_DbClient.push_data(pressure_sensor.get_qbe2002_p25_data())

        # Measurement countdown
        print(termcolor.colored("Pushing Data ...", "yellow"))
        for i in tqdm(range(100)):
            time.sleep(0.1)

        # Flow meters handling impulses to value converting
        for flow_meter in flow_meters:
            flow_meter_DbClient.push_data(flow_meter.get_data(time.time() - flow_meters_counting_start_time))

        print(termcolor.colored("Data pushed successfully", "yellow"))


start_measurments()

