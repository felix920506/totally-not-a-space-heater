import telnetlib
import serial
import json

# Read Config

with open('config.json','r',encoding='utf8') as configfile:
    options = json.load(configfile)

# host = '127.0.0.1:36330'
# enabled_slots = [0,2]
# controllerport = 'COM3'
# controllerbaud = 115200

# Setup FAH Connections

fahclients = []

class client:
    def __init__(self,host,port,slots,password=None):
        self.connection = telnetlib.Telnet(host,port)
        self.connection.read_until(b'>')
        self.slots = slots
        if password:
            self.run(f'auth {password}')

    def run(self,cmd):
        self.connection.write(bytes(cmd + '\n','utf8'))
        return self.connection.read_unti(b'>')

    def pause(self):
        cmd = 'pause'
        for slot in self.slots:
            finalcmd = cmd + ' ' + str(slot) + '\n'
            self.run(finalcmd)
    
    def unpause(self):
        cmd = 'unpause'
        for slot in self.slots:
            finalcmd = cmd + ' ' + str(slot) + '\n'
            self.run(finalcmd)

for host in options['hosts']:
    fahclients.append(client(host['ip'],host['port'],host['slots']))

# setup MCU connection

controller = serial.Serial(options['mcu']['port'], options['mcu']['baud'])

lastState = False
newState = False

def pause():
    for host in fahclients:
        host.pause()

def unpause():
    for host in fahclients:
        host.unpause()

# Throw out MCU init info and get initial state on heating/idle

init_done = False

while not init_done:
    try:
        newState = int(controller.readline().decode('utf8').strip())
    except:
        pass
    else:
        init_done = True

# Set FAHClient(s) to initial supposed to be state

if newState:
    unpause()
else:
    pause()

# continuing to watch for state changes

while True:
    try:
        newState = bool(int(controller.readline().decode('utf8').strip()))
    except:
        continue

    if not newState == lastState:
        if newState:
            unpause()
        else:
            pause()

        # for slot in enabled_slots:
        #     finalcmd = cmd + ' ' + str(slot) + '\n'
        #     fahclient.write(bytes(finalcmd,'utf8'))
        #     fahclient.read_until(b'>')
    
    lastState = newState