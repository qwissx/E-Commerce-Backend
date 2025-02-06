#!/bin/bash

cd ..
source .venv/bin/activate

sudo systemctl start docker.service
sudo docker start db
sudo docker start redis

alembic upgrade head

echo "container is working"
