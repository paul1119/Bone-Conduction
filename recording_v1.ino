#define CLOCK_PIN 9  // PWM pin for the clock signal
#define DATA_PIN 2   // Digital input pin for the microphone data
#define SWITCH_PIN 3


void setup() {
  pinMode(CLOCK_PIN, OUTPUT);
  pinMode(DATA_PIN, INPUT);
  Serial.begin(2000000);

  // Generate a 1 MHz clock signal on CLOCK_PIN
  TCCR1A = (1 << COM1A0);  // Toggle OC1A on compare match
  TCCR1B = (1 << WGM12) | (1 << CS10);  // CTC mode, no prescaler
  OCR1A = 7;  // Set output compare register for 2 MHz (16 MHz / (2 * (OCR1A + 1)))
}

void loop() {
  // Read PDM data

  // int switch_state = digitalRead(SWITCH_PIN);
  // Serial.print(switch_state);

  // if (switch_state == LOW) {
  int pdmValue = digitalRead(DATA_PIN);
  Serial.println(pdmValue);  // Send data to the serial monitor
 // }
}
