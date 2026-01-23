from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/svm_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[
        data["packet_size"],
        data["src_port"],
        data["dst_port"],
        data["protocol"],
        data["time_interval"]
    ]])

    features = scaler.transform(features)
    prediction = model.predict(features)

    return jsonify({
        "status": "anomaly" if prediction[0] == -1 else "normal"
    })
