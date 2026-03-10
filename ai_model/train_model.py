import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

np.random.seed(42)

# Generate normal readings
temperature_normal = np.random.normal(52, 4, 1000)
vibration_normal = np.random.normal(0.35, 0.08, 1000)
current_normal = np.random.normal(1.5, 0.25, 1000)

# Generate abnormal readings
temperature_fault = np.random.normal(70, 3, 50)
vibration_fault = np.random.normal(0.9, 0.15, 50)
current_fault = np.random.normal(2.8, 0.4, 50)

# Combine data
temperature = np.concatenate([temperature_normal, temperature_fault])
vibration = np.concatenate([vibration_normal, vibration_fault])
current = np.concatenate([current_normal, current_fault])

data = pd.DataFrame({
    "Temperature": temperature,
    "Vibration": vibration,
    "Current": current
})

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Save trained model
joblib.dump(model, "maintenance_model.pkl")