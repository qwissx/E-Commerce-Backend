#!/bin/bash

alembic upgrade head

uvicorn e_commerce.main:api --host 0.0.0.0 --port 8000