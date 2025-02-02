#!/bin/bash

cd ..
source .venv/bin/activate

sudo systemctl start docker.service
sudo docker start db

alembic upgrade head

echo "container is working"
