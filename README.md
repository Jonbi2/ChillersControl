# Hello!

# This program will allow You to use our data collecting device, based on RaspberryPi. It useses temperature sensors(DS18B20), flowmeters(F300A), pressure sensors(QBE2002_P25 by Siemens) and a power sensor(microDPM680). You can connect as many temperature sesnors, flowmeters, pressure sensors as You can fit on Your raspberry!

# First, connect Your sensors as shown in the electric diagram. Remember which pins You use on the raspberry

# State which pins You connect each sensor to in the config.json file

# Now, just run the bash scrip "start.sh", it will start up the rest API and it will start collecting data from all the connected sensors!

# That's it! Your database is ready and collecting data in real time. Just type in Your raspberry IP and the 5000 port and all the records will appear! You can experiment with some SQL requests too if You want

Enjoy !