import asyncio
import websockets

# Exécute une fonction de manière asynchrone pour obtenir une entrée utilisateur
async def ainput(prompt: str = "") -> str:
    return await asyncio.get_event_loop().run_in_executor(None, input, prompt)

# Fonction principale du client de chat
async def chat_client():
    # Remplacez par l'URL fournie par ngrok pour le tunnel HTTP.
    # Par exemple, pour une URL sécurisée, utilisez wss://...
    uri = "wss://innocent-lemming-moderately.ngrok-free.app"
    nickname = await ainput("Entrez votre pseudo: ")
    
    # Connexion au serveur WebSocket
    async with websockets.connect(uri) as websocket:
        # Envoie du pseudo dès la connexion
        await websocket.send(nickname)
        
        # Fonction pour recevoir les messages du serveur
        async def receiver():
            while True:
                try:
                    message = await websocket.recv()
                    print(message)
                except websockets.exceptions.ConnectionClosed:
                    print("La connexion a été fermée.")
                    break

        # Fonction pour envoyer des messages au serveur
        async def sender():
            while True:
                message = await ainput("")
                await websocket.send(f"{nickname}: {message}")

        # Exécute les tâches d'envoi et de réception en parallèle
        await asyncio.gather(receiver(), sender())

asyncio.run(chat_client())