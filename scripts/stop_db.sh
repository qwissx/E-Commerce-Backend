#!/bin/bash

sudo docker stop db
sudo systemctl stop docker.socket docker.service
echo "container and docker stoped"
