#include <ezButton.h>

ezButton bluebutton(13);
ezButton redbutton(12);

hw_timer_t *every2s = NULL;
int state = 1;

int every2svar = 0;

void IRAM_ATTR every2sSignal(){
  every2svar = 1;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  bluebutton.setDebounceTime(100);
  redbutton.setDebounceTime(100);
  every2s = timerBegin(0,80,true);
  timerAttachInterrupt(every2s, &every2sSignal, true);
  timerAlarmWrite(every2s, 2000000, true);
  timerAlarmEnable(every2s);

}

void loop() {
  // put your main code here, to run repeatedly:
  bluebutton.loop();
  redbutton.loop();
  if (bluebutton.isPressed()){
    state = 0;
  }
  if (redbutton.isPressed()){
    state = 1;
  }
  if (every2svar) {
    Serial.println(state);
    every2svar = 0;
  }

}
