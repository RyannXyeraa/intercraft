import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []

def broadcast(msg):
    dead = []

    for client in clients:
        try:
            client.send(msg)
        except:
            dead.append(client)

    for client in dead:
        clients.remove(client)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)

            if not msg:
                break

            broadcast(msg)

        except:
            break

    client.close()

    if client in clients:
        clients.remove(client)

def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server running on {PORT}")

    while True:
        client, addr = server.accept()

        print("Connected:", addr)

        clients.append(client)

        threading.Thread(
            target=handle,
            args=(client,),
            daemon=True
        ).start()

if __name__ == "__main__":
    main()
