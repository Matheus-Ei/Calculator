#!/bin/bash

git pull

# python3 -m venv .venv
# pip install -r ./requirements.txt

. ./.venv/bin/activate && python3 ./app.py
