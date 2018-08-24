import time

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

from app.routesMethods.parametersTicker import params_dict

measurment_time = json.load(open('config.json'))['MeasurmentTime']

if measurment_time is None:
    measurment_time = 25
else:
    measurment_time = int(measurment_time)



def start_measurments():
    while True: 
        # Micro Dmp680 handling
        currents = get_micro_dpm68_voltages_and_currents_data()
        powers = get_micro_dpm680_powers_data()
        microDpm680_voltage_and_currents_DbClient.push_data(currents)
        microDpm680_powers_DbClient.push_data(powers)

        # DS18B20 temperatire sensors handling 
        try:
            temperatures = get_ds18b20_data()
            ds18b20_DbClient.push_data(temperatures)
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
            pressures = pressure_sensor.get_qbe2002_p25_data()
            qbe2002p25_DbClient.push_data(pressures)

        # Measurement countdown
        print("Pushing Data ...")
        for i in tqdm(range(measurment_time)):
            time.sleep(0.1)

        # Flow meters handling impulses to value converting
        for flow_meter in flow_meters:
            flows = flow_meter.get_data(time.time() - flow_meters_counting_start_time)
            flow_meter_DbClient.push_data(flows)

        print(termcolor.colored("Data pushed successfully", "yellow"))

start_measurments()