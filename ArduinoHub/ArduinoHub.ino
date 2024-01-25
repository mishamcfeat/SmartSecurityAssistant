void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // [Initialize Wi-Fi module or other communication protocols if necessary]
}

void loop() {
  // Read data from API Gateway
  // [Code to receive data]

  // Process and send data to PC
  Serial.println("Data from Raspberry Pi nodes");
  // [Code to send data to PC]
}
