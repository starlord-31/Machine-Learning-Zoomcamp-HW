import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)
with open('model2.bin', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    # Put the below 3 lines in a seperate function when working on a real project as it's the core logic.
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[:, 1]

    result = {
        'credit_probability': float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9695)