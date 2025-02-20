#!/bin/bash

sudo docker stop db
sudo docker stop redis
sudo docker stop broker

sudo systemctl stop docker.socket docker.service

echo "container and docker stoped"
