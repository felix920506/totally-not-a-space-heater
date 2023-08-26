import telnetlib

class FAHClient:
    def __init__(self,host,port,slots,password=None):
        self.connection = telnetlib.Telnet(host,port)
        self.connection.read_until(b'>')
        self.slots = slots
        self.host = host
        self.port = port
        if password:
            self.run(f'auth {password}')

    def __del__(self):
        self.connection.write(bytes('quit\n','utf8'))

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
