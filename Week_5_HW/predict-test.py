#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://0.0.0.0:9695/predict'

client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()

print(response)