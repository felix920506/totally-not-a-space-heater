import telnetlib
import serial
import json

# Read Config

with open('config.json','r',encoding='utf8') as configfile:
    options = json.load(configfile)

# Setup FAH Connections

fahclients = []

class client:
    def __init__(self,host,port,slots,password=None):
        self.connection = telnetlib.Telnet(host,port)
        self.connection.read_until(b'>')
        self.slots = slots
        self.host = host
        self.port = port
        if password:
            self.run(f'auth {password}')

    def run(self,cmd):
        try:
            self.connection.write(bytes(cmd + '\n','utf8'))
            res = self.connection.read_until(b'>')
        except:
            print(f'failed to run command on host {self.host}:{self.port}')
        else:
            return res

    def pause(self):
        for slot in self.slots:
            self.run('pause')
    
    def unpause(self):
        for slot in self.slots:
            self.run('unpause')

for host in options['hosts']:
    if not 'port' in host:
        host['port'] = 36330
    
    if not 'pass' in host:
        host['pass'] = None

    fahclients.append(client(host['ip'],host['port'],host['enabled_slots'],host['pass']))

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
            print('Threshold reached, heating unpaused')
        else:
            pause()
            print('Threshold reached, heating paused')
    
    lastState = newState