#define PIR_SENSOR_PIN 2       // PIR sensor connected to D2
#define DOOR_SENSOR_PIN 3      // Door sensor (Reed switch) connected to D3
#define BUZZER_PIN 4           // Buzzer connected to D4

unsigned long buzzerStartTime = 0;
bool buzzerOnDueToMotion = false;

void setup() {
    Serial.begin(9600);
    pinMode(PIR_SENSOR_PIN, INPUT);
    pinMode(DOOR_SENSOR_PIN, INPUT_PULLUP);  // Door closed = HIGH, open = LOW
    pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
    int pirState = digitalRead(PIR_SENSOR_PIN);
    int doorState = digitalRead(DOOR_SENSOR_PIN);

    // Motion detected
    if (pirState == HIGH && !buzzerOnDueToMotion) {
        Serial.println("MOTION");
        digitalWrite(BUZZER_PIN, HIGH);
        buzzerStartTime = millis();
        buzzerOnDueToMotion = true;
    }

    // Handle 30sec buzzer timeout
    if (buzzerOnDueToMotion && (millis() - buzzerStartTime >= 30000)) {
        buzzerOnDueToMotion = false;
        digitalWrite(BUZZER_PIN, LOW);
    }

    // Door is open
    if (doorState == LOW) {
        Serial.println("DOOR_OPEN");
        digitalWrite(BUZZER_PIN, HIGH);
    }

    // No motion + door is closed + timeout complete
    if (pirState == LOW && doorState == HIGH && !buzzerOnDueToMotion) {
        digitalWrite(BUZZER_PIN, LOW);
    }

    delay(500);
}
