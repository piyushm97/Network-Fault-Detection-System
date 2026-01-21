import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)
    
    # Encode protocol
    df['protocol'] = df['protocol'].map({'TCP':0, 'UDP':1})
    
    # Features only
    X = df[['packet_size', 'src_port', 'dst_port', 'protocol', 'time_interval']]
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, scaler
