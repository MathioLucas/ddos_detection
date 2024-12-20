import tensorflow as tf
from keras import layers, models
import numpy as np
import os

def build_model(input_shape):
    model = models.Sequential([
        layers.LSTM(64, input_shape=input_shape, return_sequences=True),
        layers.LSTM(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(X_train, y_train, X_val, y_val, save_path="models/ddos_model.h5"):
    model = build_model((X_train.shape[1], 1))
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    model.save(save_path)

if __name__ == "__main__":
    X_train = np.load("data/processed/X_train.npy")
    y_train = np.load("data/processed/y_train.npy")
    X_val = np.load("data/processed/X_val.npy")
    y_val = np.load("data/processed/y_val.npy")
    X_train = X_train[..., np.newaxis]
    X_val = X_val[..., np.newaxis]
    train_model(X_train, y_train, X_val, y_val)
