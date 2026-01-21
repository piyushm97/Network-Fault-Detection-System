from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("models/svm_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/", methods=["GET"])
def home():
    return "Network Fault Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        packet_size = data["packet_size"]
        src_port = data["src_port"]
        dst_port = data["dst_port"]
        protocol = data["protocol"]
        time_interval = data["time_interval"]

        # Encode protocol
        protocol_encoded = 1 if protocol.upper() == "TCP" else 0

        features = np.array([[packet_size, src_port, dst_port, protocol_encoded, time_interval]])
        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)

        result = "anomaly" if prediction[0] == -1 else "normal"

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
