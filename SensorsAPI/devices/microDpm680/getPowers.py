import requests
import xmltodict
import json
import time


def get_micro_dpm680_powers_data():
    xml_response = requests.get('http://192.168.1.101/status1.xml').text
    response_json = json.dumps(xmltodict.parse(xml_response))
    response_dict = json.loads(response_json)
    data = dict(response_dict['response'])
    data.pop("Hr")
    data.pop("Mn") 
    data.pop("Dt")
    data.pop("Mt")
    data.pop("Yr")
    return data



