import requests
import xmltodict
import json
import time


def get_micro_dpm68_voltages_and_currents_data():
    address = json.load(open('config.json'))['MicroDpm680Addresses'][0]
    xml_response = requests.get('http://' + address + '/status.xml').text
    response_json = json.dumps(xmltodict.parse(xml_response))
    response_dict = json.loads(response_json)
    data = dict(response_dict['response'])
    data.pop("Hr")
    data.pop("Mn") 
    data.pop("Dt")
    data.pop("Mt")
    data.pop("Yr")
    return data



