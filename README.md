# totally-not-a-space-heater
A project attempting to control a folding@home rig based on room temperature with a microcontroller

⚠️ IMPORTANT NOTICE ⚠️
This project DOES NOT work with FAHClient v8, Please install v7 to use

## Required Materials
The following parts are required to build:
- ESP32 Micontroller (Other MCUs may work but will NOT be supported)
- 2 Buttons
- 16x2 Character LCD (Based on HD44780) using I2C interface (PCF8574)
- DHT22 Temperature and Humidity Sensor
- Wires to connect circuits together (Breadboard optional)
- Micro USB cable capable of Data transfer

## Connecting Components to ESP32
- Normally Open Terminals of one button between GND and Pin 12 (Temp Up)
- Normally Open Terminals of one button between GND and Pin 13 (Temp Down)
- For DHT22, + to VIN, Out to Pin 4, - to GND
- I2C LCD, GND to GND, VCC to VIN, SDA to Pin 21, SDL to Pin 22

## Required Environment for Programming MCU
- Arduino IDE
- Drivers for your particular MCU (Varies depending on what you get)
- Libraries below to be installed

## Required Arduino Libraries
- [Button2](https://github.com/LennartHennigs/Button2) by Lennart Hennigs
- [DHT sensor library](https://github.com/adafruit/DHT-sensor-library) by Adafruit ⚠️ **Windows Users Please do NOT install v1.3.3 or newer if you have ESP32**
- [LiquidCrystal I2C](https://github.com/johnrickman/LiquidCrystal_I2C) by Frank de Brabander

## Required Environment for controlling Folding Rig(s)
- Python3 environment (Development done on 3.10 and 3.11, 3.13+ will NOT work, 3.6+ *should* work but not tested)
- pyserial package (Install with `pip install pyserial`)
- Drivers for your MCU (Varies depending on what you get)

## Project Goals

  - [x] Start and pause Folding based on room temperature
  - [ ] Vary heat output based on heating needs
  - [x] Expand to multiple machines
  - [x] Connections over Serial
  - [ ] Connections over Wifi
  - [ ] Connections over Bluetooth
