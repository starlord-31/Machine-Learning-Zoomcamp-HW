# Testing
# Load the model from disk
import pickle
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import numpy as np

model_file = 'finalized_model.bin'

loaded_model = pickle.load(open(model_file, 'rb'))

app = Flask('value')

@app.route('/predict', methods=['POST'])
def predict():
    player_attributes = request.get_json()
    from sklearn.preprocessing import MinMaxScaler
    # Initialize a scaler
    scaler = MinMaxScaler()
    # Fit the scaler to the training features and transform
    df = pd.DataFrame([player_attributes])
    df_scaled = scaler.fit_transform(df)


    df = pd.DataFrame([player_attributes])

    # Make a prediction
    prediction = loaded_model.predict(df)
    prediction_exp = np.expm1(prediction)

    result = {
        'player_value': float(prediction_exp)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)