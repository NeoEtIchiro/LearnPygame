import asyncio
import websockets

# Ensemble pour stocker les clients connectés
# Utilisé pour éviter les doublons et gérer les connexions/déconnexions
clients = set()

# Fonction pour gérer l'enregistrement des clients
async def register(websocket):
    clients.add(websocket)

# Fonction pour gérer le désenregistrement des clients
async def unregister(websocket):
    clients.remove(websocket)

# Fonction pour diffuser un message à tous les clients connectés
# Envoie le message à tous les clients sauf celui qui l'a envoyé
async def broadcast(message, sender=None):
    # Parcours de tous les clients connectés
    for client in clients.copy():
        # Exclure le client qui envoie le message
        if client != sender:
            try:
                # Envoi du message au client
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                # Si la connexion est fermée, on le retire de l'ensemble des clients
                clients.remove(client)

# Fonction principale qui gère la connexion des clients
async def handler(websocket, path=None):
    # Enregistrement du client
    await register(websocket)
    try:
        # Le client envoie son pseudo dès la connexion
        nickname = await websocket.recv()
        await broadcast(f"{nickname} a rejoint le chat!")
        # Boucle de réception des messages du client
        async for message in websocket:
            print("Message reçu: " + message)
            await broadcast(message, sender=websocket)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Désenregistrement et annonce de déconnexion
        await unregister(websocket)
        await broadcast(f"{nickname} a quitté le chat!")

async def main():
    # Démarre le serveur WebSocket sur le port 80
    async with websockets.serve(handler, "0.0.0.0", 80):
        print("Serveur WebSocket lancé sur le port 80")
        
        # Exécute le serveur indéfiniment
        # Utilise asyncio.Future() pour garder le serveur actif
        # sans bloquer le thread principal
        await asyncio.Future()


asyncio.run(main())