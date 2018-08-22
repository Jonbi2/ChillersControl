#!/bin/bash

sudo chown pi install_dependencies.sh
sudo chown pi turn_on_interfacing.sh 

sudo chmod +x install_dependencies.sh
sudo chmod +x turn_on_interfacing.sh

sudo ./install_dependencies.sh\
sudo ./turn_on_interfacing.sh\

sudo reboot

