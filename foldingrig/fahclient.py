import telnetlib

class FAHClient:
    def __init__(self,host,port,slots,password=None):
        self.__slots = slots
        self.__host = host
        self.__port = port
        self.__password = password
        self.__connection = None
        self.__connect()

    def __connect(self):
        if not self.__connection is None:
            try:
                self.__connection = telnetlib.Telnet(self.__host,self.__port)
                self.__connection.read_until(b'>')
            
                if self.__password:
                    self.__run(f'auth {self.__password}')

            except:
                print(f'Connection to {self.__host}:{self.__port} Failed.')
                self.__connection = None

    def __del__(self):
        self.__run('quit')

    def run(self,cmd):
        self.__connect()
        if self.__connection:
            self.__connection.write(bytes(cmd + '\n','utf8'))
            res = self.connection.read_until(b'>')
            return res
        else:
            print(f'failed to run command on host {self.host}:{self.port}')
            return None

    def pause(self):
        for slot in self.__slots:
            self.__run(f'pause {slot}')
    
    def unpause(self):
        for slot in self.__slots:
            self.__run(f'unpause {slot}')
