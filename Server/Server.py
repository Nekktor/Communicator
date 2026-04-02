import websocket
import websockets
import asyncio

class Server():
    def __init__(self):
        self.connected_clients = set()


    async def handler(self, websocket):
        async for message in websocket:
            print(message)

    async def start_server(self):
        try:
            async with websockets.serve(self.handler, "localhost", 8765):
                print("Server started")
                await asyncio.Future()
        finally:
            for c in self.connected_clients:
                c.close()

if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())