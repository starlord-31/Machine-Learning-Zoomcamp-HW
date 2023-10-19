import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)
with open('model1.bin', 'rb') as model_file:
    model = pickle.load(model_file)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[:, 1]
print('credit probability', y_pred)