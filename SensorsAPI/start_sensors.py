import time
import termcolor

from tqdm import tqdm

from devices.microDpm680.getData import get_micro_dpm680_data
from devices.DS18B20.getData import get_ds18b20_data

from SqlModeling.microDpm680DatabaseClient import microDpm680_DbClient
from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient

while True:
    microDpm680_DbClient.push_data(get_micro_dpm680_data())
    ds18b20_DbClient.push_data(get_ds18b20_data())
    print(termcolor.colored("Data pushed successfully", "yellow"))
    for i in tqdm(range(100)):
        time.sleep(0.1)


