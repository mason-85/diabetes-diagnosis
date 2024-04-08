from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model from the file
model = joblib.load('rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using the model loaded from disk as per the data.
    prediction = model.predict([data['input']])

    # Return the entire prediction
    output = prediction.tolist()  # Convert numpy array to list

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

