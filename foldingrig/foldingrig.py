import telnetlib
import serial
import json

with open('config.json','r',encoding='utf8') as configfile:
    options = json.load(configfile)

host = '127.0.0.1:36330'
enabled_slots = [0,2]
controllerport = 'COM3'
controllerbaud = 115200

fahclients = []

class client:
    def __init__(self,host,port,slots):
        self.connection = telnetlib.Telnet(host,port)
        self.connection.read_until(b'>')
        self.slots = slots

    def pause(self):
        cmd = 'pause'
        for slot in self.slots:
            finalcmd = cmd + ' ' + str(slot) + '\n'
            self.connection.write(bytes(finalcmd,'utf8'))
            self.connection.read_until(b'>')
    
    def unpause(self):
        cmd = 'unpause'
        for slot in self.slots:
            finalcmd = cmd + ' ' + str(slot) + '\n'
            self.connection.write(bytes(finalcmd,'utf8'))
            self.connection.read_until(b'>')


for host in options['hosts']:
    fahclients.append(client(host['ip'],host['port'],host['slots']))

controller = serial.Serial(options['mcu']['port'], options['mcu']['baud'])

lastState = False

def pause():
    for host in fahclients:
        host.pause()

def unpause():
    for host in fahclients:
        host.unpause()


# get initial slot info

# fahclient.write(b'slot-info\n')
# fahclient.read_until(b'PyON 1 slots')
# slots = eval(fahclient.read_until(b'\n---\n>')[:-6], {}, {})

# for slot in slots:
#     print(slot['options']['paused'])

while True:
    try:
        newState = bool(int(controller.readline().decode('utf8').strip()))
    except:
        continue

    if not newState == lastState:
        if newState == True:
            unpause()
        else:
            pause()

        # for slot in enabled_slots:
        #     finalcmd = cmd + ' ' + str(slot) + '\n'
        #     fahclient.write(bytes(finalcmd,'utf8'))
        #     fahclient.read_until(b'>')
    
    lastState = newState