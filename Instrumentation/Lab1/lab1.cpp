// C++ code
//

//int LEDpin=4;
  
/*void setup()
{
  pinMode(3, OUTPUT);
  pinMode(LEDpin, OUTPUT);
  
  analogWrite(3, 1);
}

void loop()
{
  	digitalWrite(LEDpin, HIGH);
	delay(1000); // Wait for 1000 millisecond(s)
  	digitalWrite(LEDpin, LOW);
  	delay(1000); // Wait for 1000 millisecond(s)
}
*/
int LEDpin=4;
int ldrvalue = 0;
int ldrpin = A5;
void setup(){
  	Serial.begin(9600);
  	pinMode(ldrpin,INPUT);
  	pinMode(LEDpin,OUTPUT);
}
void loop(){
  	ldrvalue = analogRead(ldrpin);
  	Serial.print("The value of ldr is ");
  	Serial.println(ldrvalue);
  if(ldrvalue>100){
  	digitalWrite(LEDpin, LOW);
  }
  else{
  	digitalWrite(LEDpin, HIGH);
  }
}
