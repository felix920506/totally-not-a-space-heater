//#include <ezButton.h>
#include <Button2.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE 22

Button2 bluebutton(13);
Button2 redbutton(12);

LiquidCrystal_I2C lcd(0x27,16,2);

DHT tempsense(DHTPIN,DHTTYPE);

hw_timer_t *every2s = NULL;
int every2svar = 0;
int state = 0;

float settemp = 25;
int lastinteraction = -10000;
int firstsatisfy = 0;

float roomtemp = 0;

void IRAM_ATTR every2sSignal(){
  every2svar = 1;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(1,0);
  lcd.print("Totally Not a");
  lcd.setCursor(2,1);
  lcd.print("Space Heater");

  delay(3000);

  every2s = timerBegin(0,80,true);
  timerAttachInterrupt(every2s, &every2sSignal, true);
  timerAlarmWrite(every2s, 2000000, true);
  timerAlarmEnable(every2s);

  lastinteraction = millis();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("RT=    C ");

  bluebutton.setTapHandler(bluebuttonpressed);
  redbutton.setTapHandler(redbuttonpressed);
}

void loop() {
  // put your main code here, to run repeatedly:
  bluebutton.loop();
  redbutton.loop();
  // if (bluebutton.wasPressed()){
  //   settemp -= 0.5;
  //   lastinteraction = millis();
  //   Serial.print(settemp);
  // }
  // if (redbutton.wasPressed()){
  //   settemp += 0.5;
  //   lastinteraction = millis();
  //   Serial.print(settemp);
  // }
  if (every2svar) {
    roomtemp = tempsense.readTemperature();
    if (millis() - lastinteraction >= 10000){
      lcd.setCursor(3,0);
      if(roomtemp >= 0) {
        lcd.print(roomtemp,1);
      }
      else {
        lcd.print(" <0 ");
      }
    }

    if (roomtemp - settemp >= 0.5){
      state = 0;
    }
    else if (settemp - roomtemp >= 0.5) {
      state = 1;
    }
    
    lcd.setCursor(9,0);
    if(state == 0){
      lcd.print("Idle   ");
    }
    else {
      lcd.print("Heating");
    }

    Serial.println(state);
    every2svar = 0;
  }

  if(millis() - lastinteraction >= 7000){
    lcd.setCursor(0,0);
    lcd.print("RT=");
    lcd.print(roomtemp,1);
  }
  else {
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("ST=");
    lcd.print(settemp,1);
  }
  
  if(millis() - lastinteraction >= 20000){
    lcd.noBacklight();
  }

}

void bluebuttonpressed(Button2& btn){
  settemp -= 0.5;
  lastinteraction = millis();
}

void redbuttonpressed(Button2& btn){
  settemp += 0.5;
  lastinteraction = millis();
}
