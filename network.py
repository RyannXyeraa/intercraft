import socket
import threading

class ChatClient:

    def __init__(self):
        self.sock = None

    def connect(self, host, port):

        self.sock = socket.socket()

        self.sock.connect((host, port))

        threading.Thread(
            target=self.receive,
            daemon=True
        ).start()

    def receive(self):

        while True:
            try:
                msg = self.sock.recv(1024).decode()

                if msg:
                    print("\n" + msg)

            except:
                break

    def send(self, msg):

        if self.sock:
            self.sock.send(msg.encode())
