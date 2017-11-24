
int LEDpin1 = 5;

void setup() {
  pinMode(LEDpin1, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  
  if (Serial.available() > 0) {
    char serialListener = Serial.read();
    if (serialListener == '1') {
      digitalWrite(LEDpin1, HIGH);
    }
    else if (serialListener == '0') {
      digitalWrite(LEDpin1, LOW);
    }

    }
  }
}

