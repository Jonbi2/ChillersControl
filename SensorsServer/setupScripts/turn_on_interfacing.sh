#!/bin/bash

# Enable SPI interface
sudo python3 edit_configs.py -/boot/config.txt -dtparam=spi= -on

# Enable one-wire interface
sudo python3 edit_configs.py -/boot.config.txt -dtoverlay= -w1-gpio

# Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

# Enable I2C interfacing
sudo python3 edit_configs.py -/etc/modules -i2c-dev 
sudo python3 edit_configs.py -/boot.config.txt -dtparam=i2c_arm= -on
sudo python3 edit_configs.py -/boot.config.txt -dtparam=i2c1= -on
