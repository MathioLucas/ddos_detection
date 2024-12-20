import numpy as np
import pandas as pd
import os

def generate_traffic_data(num_samples=1000):
    np.random.seed(42)
    data = {
        "cpu_usage": np.random.uniform(0, 100, num_samples),
        "memory_load": np.random.uniform(0, 100, num_samples),
        "network_traffic": np.random.uniform(0, 1000, num_samples),
        "label": np.random.choice([0, 1], size=num_samples, p=[0.95, 0.05])
    }
    return pd.DataFrame(data)

def save_traffic_data(df, save_path="data/raw/synthetic_traffic.csv"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Traffic data saved to {save_path}")

if __name__ == "__main__":
    traffic_data = generate_traffic_data(num_samples=10000)
    save_traffic_data(traffic_data)
