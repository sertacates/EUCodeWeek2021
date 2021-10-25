byte durum = 0;
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(A0, INPUT);
}
void loop()
{ durum = digitalRead(A0);
  if (durum == 1)
  {
    digitalWrite(13, HIGH);
    tone(12, 80);
    delay(1000);
    durum = 0;
  }
  else
  {
    digitalWrite(13, LOW);
    noTone(12);
    delay(25);
  }
}
