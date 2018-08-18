import time
import termcolor

from tqdm import tqdm

from devices.microDpm680.getData import get_micro_dpm680_data
from devices.DS18B20.getData import get_ds18b20_data
from devices.flowMeter.getData import flow_meters

from SqlModeling.microDpm680DatabaseClient import microDpm680_DbClient
from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

def start_measurments():
    while True: 
        # Micro Dmp680 handling
        microDpm680_DbClient.push_data(get_micro_dpm680_data())

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

        # Measurement countdown
        print(termcolor.colored("Data pushed successfully", "yellow"))
        for i in tqdm(range(100)):
            time.sleep(0.1)

        # Flow meters handling impulses to value converting
        for flow_meter in flow_meters:
            flow_meter_DbClient.push(flow_meter.get_data(time.time() - flow_meters_counting_start_time))


start_measurments()

