import socket
import threading

HOST = '0.0.0.0'  # écoute sur toutes les interfaces réseau
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []      # liste des connexions clients
nicknames = []    # liste des pseudos associés

def broadcast(message, _client):
    """Diffuser le message à tous les clients sauf l'émetteur"""
    for client in clients:
        if client != _client:
            try: 
                client.send(message)
            except:
                remove_client(client)

def handle(client):
    """Gestion de la réception des messages d'un client"""
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                print("Message reçu: " + msg.decode('utf-8'))
                broadcast(msg, client)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break

def remove_client(client):
    """Supprime le client de la liste en cas de déconnexion"""
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        nicknames.pop(index)

def receive():
    """Accepte les connexions entrantes et démarre le thread de gestion pour chaque client"""
    print("Le serveur est en écoute...")
    while True:
        client, address = server.accept()
        print("Connecté à: " + str(address))
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Le pseudo du client est: " + nickname)
        broadcast((nickname + " a rejoint le chat!").encode('utf-8'), client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Le serveur est démarré...")
receive()