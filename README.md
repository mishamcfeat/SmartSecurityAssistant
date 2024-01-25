# Smart Security Assistant

## Overview
The Smart Security Assistant is an advanced IoT-enabled home security system. It integrates a network of Raspberry Pi devices equipped with sensors and cameras to monitor, detect, and respond to various security scenarios using real-time data processing and machine learning.

## Objective
To develop a reliable, efficient, and intelligent security system leveraging IoT, machine learning, and real-time data processing to enhance home security. The system is designed to provide a scalable and comprehensive approach to security, combining sensor data management with live video streaming.

## Hardware Requirements
- **Raspberry Pi 5**: Acts as sensor nodes and camera streamers.
- **Camera Module**: For live video feeds and facial recognition.
- **PIR Motion Sensor**: Detects movement, activating the camera and lights.
- **DHT22 Sensor**: Measures temperature and humidity.
- **IR LED Lights**: Illuminate areas for the camera under low light conditions.
- **Wi-Fi Module**: For network connectivity across all Raspberry Pi nodes.

## Software Requirements
- **Operating System**: Raspberry Pi OS.
- **Programming Languages**: Python for machine learning and camera interface, C++ for Arduino programming.
- **MQTT Protocol**: For efficient sensor data transmission between Raspberry Pi nodes and Arduino.
- **Golang**: For API Gateway handling sensor data and video streams.
- **Node.js with InfluxDB**: Backend server for data processing and storage.
- **Grafana and Prometheus**: For data visualization and system monitoring.

## System Architecture
- **Raspberry Pi Nodes**: Handle sensor data collection and camera streaming.
- **MQTT Broker**: Facilitates message communication within the system.
- **Arduino Uno**: Aggregates sensor data and communicates with the Golang API Gateway.
- **Golang API Gateway**: Manages and routes sensor data and video streams.
- **Node.js Server**: Processes data and handles storage in InfluxDB.
- **Grafana and Prometheus**: Provide data visualization and monitoring.

## Functionality
- **Real-Time Data Processing**: Handles sensor data and video streams in real-time.
- **Facial Recognition and Motion Detection**: Uses machine learning for intelligent monitoring.
- **Automated Responses**: Activates alarms or notifications based on detected events.
- **Remote Access and Monitoring**: Provides access to live feeds and sensor data via a web interface.
- **Data Visualization and Alerts**: Custom dashboards for data monitoring and alert configurations.

## File Structure
- `README.md`: The main documentation file for the project.
- `/RaspberryPiNodes`: Contains scripts for Raspberry Pi nodes.
  - `/CameraModule`: Handles camera operations and facial recognition.
    - `Camera.py`: Manages camera feed.
    - `FacialRecognition.py`: Implements facial recognition using OpenCV.
  - `/SensorModule`: Scripts for handling sensor data.
    - `DHT22Sensor.py`: Manages DHT22 Temperature/Humidity Sensor.
    - `PIRsensor.py`: Manages PIR Motion Sensor.
    - `LEDcontrol.py`: Controls LED Lights.
  - `main.py`: Main script for initializing and running Raspberry Pi node functionalities.
- `/MQTTBroker`: MQTT broker configuration and setup files.
- `/GolangAPIGateway`: Contains the Golang API Gateway.
  - `main.go`: Main Golang server file.
  - `go.mod`: Golang module file.
  - `go.sum`: Golang module checksum file.
- `/ArduinoHub`: Contains the Arduino sketch.
  - `ArduinoHub.ino`: Arduino sketch for aggregating and forwarding sensor data.
- `/NodeServer`: Node.js server and InfluxDB setup.
  - `Server.js`: Main Node.js server file.
  - `InfluxdbSetup.js`: Script for setting up InfluxDB.
  - `Package.json`: Node.js project manifest.
- `/GrafanaPrometheus`: Monitoring tools configuration and setup.
  - `/prometheus`: Prometheus configuration and setup files.
  - `/grafana`: Grafana dashboards and setup files.
- `requirements.txt`: Required Python libraries.

## Implementation Steps
1. Install and configure necessary software on Raspberry Pi nodes and PC.
2. Assemble and program the hardware components (sensors, Arduino, Raspberry Pi).
3. Set up the MQTT Broker for intra-system communication.
4. Develop and deploy the Golang API Gateway.
5. Configure the Node.js server with InfluxDB for backend processing.
6. Create and set up Grafana dashboards and Prometheus monitoring.
7. Integrate all components, test the system, and refine for reliable operation.

## Getting Started
1. Clone the repository to your Raspberry Pi and PC.
2. Follow the installation instructions in `INSTALL.md`.
3. Assemble hardware components as per the provided setup guide.
4. Execute initialization scripts to configure and start the system.

## Contributions
We welcome contributions to the Smart Security Assistant project. Please refer to `CONTRIBUTING.md` for contribution guidelines.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
