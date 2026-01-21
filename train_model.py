import joblib
from sklearn import svm
from app.preprocess import load_and_preprocess

# Load and preprocess data
X, scaler = load_and_preprocess('data/raw/network_traffic.csv')

# Train One-Class SVM for anomaly detection
model = svm.OneClassSVM(kernel='rbf', gamma='auto', nu=0.1)
model.fit(X)

# Save model and scaler
joblib.dump(model, 'models/svm_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

print("Model and scaler saved successfully!")
