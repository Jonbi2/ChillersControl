#!/bin/bash

sudo apt-get install build-essential
sudo apt-get install python3
sudo apt-get install pip3
sudo apt-get install virtualenv
sudo apt-get install screen

cd .. 

virtualenv venv

source venv/bin/activate

pip3 install requests
pip3 install xmltodict
pip3 install termcolor
pip3 install tqdm
pip3 install sqlalchemy 
pip3 install flask
pip3 install flask_restful
pip3 install multitasking
pip3 install w1thermsensor
pip3 install flask_cors

cd setupScripts/