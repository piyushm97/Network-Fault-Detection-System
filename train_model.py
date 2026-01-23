import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import joblib
import os

data = pd.read_csv("data/sample_network_data.csv")

X = data[[
    "packet_size",
    "src_port",
    "dst_port",
    "protocol",
    "time_interval"
]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = OneClassSVM(kernel="rbf", gamma="auto", nu=0.05)
model.fit(X_scaled)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/svm_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model training completed successfully")
