import telnetlib
import serial

host = '127.0.0.1:36330'
enabled_slots = [0,2]
controllerport = 'COM3'
controllerbaud = 115200

fahclient = telnetlib.Telnet('localhost',36330)
controller = serial.Serial(controllerport, controllerbaud)
lastState = False

fahclient.read_until(b'>')

while True:
    try:
        newState = bool(int(controller.readline().decode('utf8').strip()))
    except:
        continue

    if not newState == lastState:
        if newState == True:
            cmd = 'unpause'
        else:
            cmd = 'pause'

        for slot in enabled_slots:
            finalcmd = cmd + ' ' + str(slot) + '\n'
            fahclient.write(bytes(finalcmd,'utf8'))
    
    lastState = newState

