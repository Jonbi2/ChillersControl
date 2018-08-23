#Repository structure

######This reposotory contains two projects the SensorsServer and the SensorsReactClient

#SensorsServer

######This subproject is a collection of scripts which collect data from sensors such as DS18B20 temperature sensors, F300A flow meters, 
######Siemiens QBE2002_P25 pressure sensors, MicroDpm680 power and voltage measurer. The next part of the Server pushes the data and ######stores it in a SQLite database locally and provides an REST API to get this data and monitor how is the device working.  

#SensorsReactClient 

######This subproject is a React WebApp which communicates with the REST server to just show the data and interact with that, for example ######show realtime measurments in a table, download .csv or .json files according a specific parameter in a timerange. 
######Next features will allow to config the logic and conditions when a device will start or stop and report executive machines such ######compressors, pomps anomalies.

#How to start it? 

######1.Get an Raspberry pi and connect all the devices and specify the pins where the devices will be connected. 
######2.Get the raspberryPi address and input this address in the SensorsReactClient/src/config.json file
######3.Download the SensorsServer on the RaspberryPi and run all the setup scripts 
######4.Run the server on the RaspberryPi and run the ReactClient on a different device using yarn start and installing the dependencies. 