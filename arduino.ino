const int LED_PIN = 10; 

void setup() {
    pinMode(LED_PIN, OUTPUT);
    Serial.begin(9600); 
}

void loop() {
    if (Serial.available()) { 
        char command = Serial.read(); 
        if (command == '1') {
            digitalWrite(LED_PIN, HIGH); 
        } else if (command == '0') {
            digitalWrite(LED_PIN, LOW); 
        }
    }
}