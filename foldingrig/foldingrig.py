import serial
import json
from fahclient import FAHClient as client
import os

CONFIGPATH = './config.json'

loadconfigerror = False

# Read Config
if os.path.isfile(CONFIGPATH):
    try:
        with open('config.json', 'r', encoding='utf8') as configfile:
            options = json.load(configfile)

    except:
        loadconfigerror = True
        print('Could not load "config.json". Maybe another program is using the file, permissions are misconfigured, or it is not a valid JSON file.')

elif os.path.isdir(CONFIGPATH):
    loadconfigerror = True
    print('"config.json" is a directory, abort.')

else:
    with open('config.json', 'w+', encoding='utf8') as configfile:
        options = {
            'hosts': [
                {'ip': '127.0.0.1', 'port': 36330, 'enabled_slots': [0,1]},
                {'ip': 'example.com', 'port': 12345, 'enabled_slots': [0,1,2,3]}
            ],
            'mcu': {
                'port': 'COM3', 'baud': 115200
            }
        }

        json.dump(options, configfile, indent=4)
    
    loadconfigerror = True
    print('Created sample config file. Please edit with appropriate settings.')



# main program logic

if __name__ == '__main__' and not loadconfigerror:

    print('Starting...')

    # Setup FAH Connections

    fahclients = []
    #     def __init__(self,host,port,slots,password=None):
    #         self.connection = telnetlib.Telnet(host,port)
    #         self.connection.read_until(b'>')
    #         self.slots = slots
    #         self.host = host
    #         self.port = port
    #         if password:
    #             self.run(f'auth {password}')

    #     def __del__(self):
    #         self.connection.write(bytes('quit\n','utf8'))

    #     def run(self,cmd):
    #         try:
    #             self.connection.write(bytes(cmd + '\n','utf8'))
    #             res = self.connection.read_until(b'>')
    #         except:
    #             print(f'failed to run command on host {self.host}:{self.port}')
    #         else:
    #             return res

    #     def pause(self):
    #         for slot in self.slots:
    #             self.run('pause')
        
    #     def unpause(self):
    #         for slot in self.slots:
    #             self.run('unpause')

    for host in options['hosts']:
        if not 'port' in host:
            host['port'] = 36330
        
        if not 'pass' in host:
            host['pass'] = None

        fahclients.append(client(host['ip'],host['port'],host['enabled_slots'],host['pass']))

    # setup MCU connection

    controller = serial.Serial(options['mcu']['port'], options['mcu']['baud'],timeout=10)

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
        except TimeoutError:
            coutroller = serial.Serial(options['mcu']['port'], options['mcu']['baud'],timeout=10)
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
