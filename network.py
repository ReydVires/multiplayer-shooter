import socket
import pickle


class Network:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip  # Server IP
        self.port = port
        self.buffer = 1024
        self.addr = (self.server, self.port)
        self.player_data = self.connect()

    def player(self):
        return self.player_data

    def set_buffer(self, value):
        self.buffer = value

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(self.buffer))  # return object
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))  # sending object
            return pickle.loads(self.client.recv(self.buffer))
        except socket.error as e:
            print(e)
