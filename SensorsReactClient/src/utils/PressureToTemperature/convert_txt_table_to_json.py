# Usage: python3 convert_txt_table_to_json.py -file_name
# file_name.txt will be converted to file_name.json
# Example :
# Input file : R404A.txt
# python3 convert_txt_table_to_json.py -R404A
# Output R404A.json 

import sys
import json


file_name = str(sys.argv[1])[1:] 

with open(file_name + '.txt', "r") as file:
    values = {}
    for line in file:
        value = line.split('	')
        for i in range(0, len(value)):
            value[i] = value[i].replace(',', '.')     
            value[i] = value[i].replace('\n', '')    
        values[value[0]] = float(value[1])

with open(file_name + '.json', 'w+') as json_file:
    json.dump(values, json_file)
