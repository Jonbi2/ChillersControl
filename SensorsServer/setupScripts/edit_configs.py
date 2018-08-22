import sys
import fileinput

file_path = str(sys.argv[1])[1:]
config = str(sys.argv[2])[1:]

if sys.argv[3] is None:
    parameter = ""
parameter = str(sys.argv[3])[1:]

logfile = open(file_path, 'r')
loglist = logfile.readlines()
logfile.close()

def replace_line(text_to_be_replaced, replace_text):
    for i, line in enumerate(fileinput.input(file_path, inplace=1)):
        sys.stdout.write(line.replace(str(text_to_be_replaced), str(replace_text)))

def is_line_existing(text_line):
    for line in loglist:
        if str(text_line) in line:
            return True
    return False

def get_negated_parameter(param):
    if param == 'on':
        return 'off'
    if param == 'off':
        return 'on'


if not is_line_existing(config + "on") and not is_line_existing(config + "off"):
    with open(file_path, "r+") as file:
        old = file.read() 
        file.seek(0) 
        file.write(config + parameter + "\n" + old) 
    exit(0)

if is_line_existing(config + get_negated_parameter(parameter)):
    replace_line(config + get_negated_parameter(parameter), config + parameter)
    exit(0)



