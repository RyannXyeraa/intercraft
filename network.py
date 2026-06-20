import socket
import threading
from utils import print_chat

class ChatClient:
    def __init__(self):
        self.sock = None
        self.running = False

    def connect(self, host, port=5000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.running = True

        thread = threading.Thread(target=self._listen, daemon=True)
        thread.start()

    def _listen(self):
        while self.running:
            try:
                msg = self.sock.recv(1024).decode()
                if msg:
                    print_chat(msg)
            except:
                break

    def send(self, msg):
        if self.sock:
            try:
                self.sock.send(msg.encode())
            except:
                pass


class ChatServer:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port
        self.clients = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

    def broadcast(self, msg, sender):
        for c in self.clients:
            if c != sender:
                try:
                    c.send(msg)
                except:
                    self.clients.remove(c)

    def handle(self, conn):
        self.clients.append(conn)

        while True:
            try:
                msg = conn.recv(1024)
                if not msg:
                    break
                self.broadcast(msg, conn)
            except:
                break

        self.clients.remove(conn)
        conn.close()

    def start(self):
        print(f"[SERVER] Running on {self.port}")

        while True:
            conn, addr = self.server.accept()
            print("[NEW]", addr)

            thread = threading.Thread(
                target=self.handle,
                args=(conn,),
                daemon=True
            )
            thread.start()
