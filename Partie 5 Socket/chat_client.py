import socket
import threading

HOST = '127.0.0.1'  # Remplacer par l'adresse IP du serveur si nécessaire
PORT = 12345

nickname = input("Choisis ton pseudo: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    """Thread de réception des messages du serveur"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Une erreur est survenue!")
            client.close()
            break

def write():
    """Thread d'envoi des messages saisis par l'utilisateur"""
    while True:
        message = "{}: {}".format(nickname, input(''))
        client.send(message.encode('utf-8'))

# Démarrage des threads de réception et d'envoi
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()