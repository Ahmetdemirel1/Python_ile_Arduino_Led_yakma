int LEDpin1 = 5;


void setup() {
  pinMode(LEDpin1, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()){
    char serialListener = Serial.read();
    if (serialListener = 'LedOn'){
      digitalWrite(LEDpin1, HIGH);
    }
    else if (serialListener = 'LedOff'){
      digitalWrite(LEDpin1, LOW);
    }              
  }
}
