# industry-machine-maintanence-system
AI-based smart machine maintenance system for industry 5.0
# Industry 5.0 Machine Maintenance System



The Industry 5.0 Machine Maintenance System is an IoT-based predictive maintenance platform designed to monitor industrial machines using sensors and detect anomalies using machine learning.

The system collects sensor data from ESP32 devices, sends it through MQTT, processes it using a FastAPI backend, and displays the machine status on a web dashboard built using HTML, CSS, and JavaScript.

Technicians can also provide feedback which helps in improving the monitoring process.

workflow:

ESP32 Sensors
↓
MQTT Communication
↓
FastAPI Backend
↓
SQLite Database
↓
Machine Learning Model (Anomaly Detection)
↓
Web Dashboard (HTML, CSS, JavaScript)
---
file management:

Industry5_Machine_Maintenance_System
│
├── hardware
│   └── esp32_sensor_code
│
├── backend
│   ├── main.py                 # FastAPI server entry point
│   ├── api_server.py           # API endpoints
│   ├── mqtt_receiver.py        # Receives sensor data from MQTT broker
│   ├── anomaly_detection.py    # Machine learning anomaly detection
│   ├── feedback_loop.py        # Technician feedback processing
│
├── database
│   └── database.db             # SQLite database storing machine data
│
├── ai_model
│   └── trained_model.pkl       # Trained machine learning model
│
├── frontend
│   ├── index.html              # Dashboard interface
│   ├── style.css               # Dashboard styling
│   ├── dashboard.js            # API communication with backend
│   └── charts.js               # Sensor data visualization
│
├── requirements.txt            # Python dependencies
└── README.md
```

The backend is built using FastAPI and handles:

• Receiving sensor data
• Running anomaly detection
• Storing machine data
• Providing APIs for the dashboard
• Managing technician feedback

Main backend modules:

main.py-Starts the FastAPI server.
mqtt_receiver.py-Receives sensor data from ESP32 using MQTT.
anomaly_detection.py-Loads the trained ML model and predicts machine anomalies.
feedback_loop.py-Stores technician feedback for prediction validation.
api_server.py-Defines REST API endpoints used by the dashboard.
---

Database

The system uses SQLite database.

Database file:

```
database/database.db
```

Example tables:

• sensor_data
• anomaly_predictions
• technician_feedback

---

 AI Model

The machine learning model is stored as:

```
ai_model/trained_model.pkl
```

The model analyzes sensor parameters such as:

• Temperature
• Vibration
• Pressure

to detect abnormal machine behavior.

---
Frontend Dashboard

The dashboard is built using:

• HTML
• CSS
• JavaScript

It provides:

• Machine health status
• Sensor data monitoring
• Anomaly alerts
• Technician feedback interface
• Data visualization charts

---

 Technologies Used

Backend

* Python
* FastAPI
* Uvicorn
* SQLite
* Paho MQTT
* Scikit-Learn
* Joblib
* Pandas
* NumPy

Frontend

* HTML
* CSS
* JavaScript
* Chart.js

Hardware

* ESP32
* Industrial Sensors

---


Future Improvements

• Real-time WebSocket updates
• Cloud deployment
• Advanced machine learning models
• Mobile application dashboard
• Predictive maintenance alerts

---


