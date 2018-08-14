#!/bin/bash

cd ..
mv dummysandbox BolidLab
cd BolidLab

virtualenv venv
source venv/bin/activate
sh install_dependencies.sh
