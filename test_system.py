import numpy as np
from anomaly_detection import load_model, detect_anomaly
from resource_alert import alert_system

def test_system(num_tests=10):
    print("Starting system test...\n")
    model = load_model()
    for i in range(num_tests):
        test_data = np.random.rand(3)
        detection_result = detect_anomaly(model, test_data)
        print(f"Test {i + 1}: {detection_result}")
        alert_system(detection_result)
        print("-" * 50)

if __name__ == "__main__":
    test_system(num_tests=5)
