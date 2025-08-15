// Define Motor A connections
#define enA 8    // Enable pin (No PWM, so use digitalWrite HIGH)
#define in1 9    // Direction pin
#define in2 10   // Direction pin

// Define Motor B connections
#define enB 13   // Enable pin
#define in3 11   // Direction pin
#define in4 12   // Direction pin

// Define Motor C connections
#define enC 3    // Enable pin
#define in5 6    // Direction pin
#define in6 7    // Direction pin

void setup() {
    Serial.begin(9600); // Start Serial Monitor
    
    // Set motor control pins as outputs
    pinMode(enA, OUTPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    
    pinMode(enB, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);

    pinMode(enC, OUTPUT);
    pinMode(in5, OUTPUT);
    pinMode(in6, OUTPUT);

    Serial.println("Motors Initialized!");

    // Enable motors
    digitalWrite(enA, HIGH);  // Motor A enabled (pin 8 HIGH)
    digitalWrite(enB, HIGH);  // Motor B enabled
    digitalWrite(enC, HIGH);  // Motor C enabled

    delay(500);  // Allow motors to initialize
}

void loop() {
    Serial.println("Moving Forward...");
    
    // Move Motor A forward
    digitalWrite(in1, HIGH);  // Motor A forward direction
    digitalWrite(in2, LOW);   // Motor A forward direction
    
    // Move Motor B forward
    digitalWrite(in3, HIGH);  // Motor B forward direction
    digitalWrite(in4, LOW);   // Motor B forward direction
    
    // Move Motor C forward (keep rolling)
    digitalWrite(in5, HIGH);  // Motor C forward direction
    digitalWrite(in6, LOW);   // Motor C forward direction
    
    delay(3000);  // All motors move forward for 3 seconds

    Serial.println("Moving Backward...");
    
    // Move Motor A backward
    digitalWrite(in1, LOW);   // Motor A reverse direction
    digitalWrite(in2, HIGH);  // Motor A reverse direction
    
    // Move Motor B backward
    digitalWrite(in3, LOW);   // Motor B reverse direction
    digitalWrite(in4, HIGH);  // Motor B reverse direction
    
    // Motor C keeps rolling forward (no change for C)
    // No need to modify `in5` and `in6` for Motor C

    delay(3000);  // All motors move backward for 3 seconds

    Serial.println("Rolling Motor C...");

    // Keep Motor C rolling forward continuously
    digitalWrite(in5, HIGH);  // Motor C forward direction
    digitalWrite(in6, LOW);   // Motor C forward direction

    // No delay, so Motor C continues running
}
