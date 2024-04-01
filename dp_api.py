from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the model from the file
model = load_model('trained_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using the model loaded from disk as per the data.
    prediction = model.predict([np.array([data['input']])])

    # Return the entire prediction
    output = prediction.tolist()  # Convert numpy array to list

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

