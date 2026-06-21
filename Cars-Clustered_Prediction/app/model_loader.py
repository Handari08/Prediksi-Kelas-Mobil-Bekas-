import joblib
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "rf_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "model", "scaler.pkl")


model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


cluster_labels = {
    0: 'Mobil Harian Modern',
    1: 'Mobil Bekas Ekonomis',
    2: 'Mobil Performa Tinggi',
    3: 'Mobil Premium'
}