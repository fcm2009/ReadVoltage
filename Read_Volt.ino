int delay_time = 500;
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  float volt = analogRead(A0) * 5.0/1023.0;
  Serial.println(volt);
  delay(delay_time);
}
