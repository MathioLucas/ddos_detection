import tensorflow as tf
import numpy as np

def load_model(model_path="models/ddos_model.h5"):
    return tf.keras.models.load_model(model_path)

def detect_anomaly(model, data_point):
    prediction = model.predict(data_point[np.newaxis, ..., np.newaxis])
    return "Potential DDoS Attack" if prediction > 0.5 else "Normal Traffic"

if __name__ == "__main__":
    model = load_model()
    test_data = np.random.rand(3)
    result = detect_anomaly(model, test_data)
    print(f"Detection Result: {result}")
