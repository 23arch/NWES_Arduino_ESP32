void setup(){
// put your setup code here, to run once:
pinMode(27, OUTPUT);
pinMode(33, OUTPUT);
}

void loop() {
// put your main code here, to run repeatedly:
digitalWrite(27, HIGH);
delay(700);
digitalWrite(27, LOW);
delay(700);
digitalWrite(33, HIGH);
delay(700);
digitalWrite(33, LOW);
delay(700);
}
