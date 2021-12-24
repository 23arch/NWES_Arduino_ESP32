int interruptCounter=NULL;
hw_timer_t * timer
= NULL;
void onTime ()
{
interruptCounter++;
if(interruptCounter % 2 == 1)
{
digitalWrite (27, HIGH) ;
digitalWrite (33, LOW) ;
}
else
{
digitalWrite (27, LOW);
digitalWrite (33, HIGH);
}
}
void setup ()
{
pinMode (15, LOW);
pinMode (27, OUTPUT) ;
digitalWrite (27, LOW);
timer = timerBegin (0, 150, true) ;
timerAttachInterrupt (timer, onTime, true) ;
timerAlarmWrite(timer, 500000, true) ;
timerAlarmEnable(timer);

pinMode (33, OUTPUT) ;
digitalWrite (33, LOW);
timer = timerBegin (0, 150, true) ;
timerAttachInterrupt (timer, onTime, true) ;
timerAlarmWrite(timer, 500000, true) ;
timerAlarmEnable(timer);
}
void loop()
{
}
