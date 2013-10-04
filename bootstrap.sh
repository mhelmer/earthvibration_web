#!/bin/bash
virtualenv .env
source .env/bin/activate
pip install --upgrade setuptools
pip install -r requirements.txt
