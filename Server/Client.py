import websockets
import asyncio
url = "ws://localhost:8765"

class Client:
    def __init__(self):
        pass

    async def connect(self):
        async with websockets.connect(url) as websocket:
            try:
                await websocket.send("Hello")
            except Exception as e:
                print(e)


if __name__ == "__main__":
    client = Client()
    asyncio.run(client.connect())