import json

import websockets
import asyncio

class Server():
    def __init__(self):
        self.connected_clients = set()
        self.action_handlers = {
            "auth" : self.auth
        }

    async def handler(self, websocket):
        try:
            async for message in websocket:
                t_message = json.loads(message)
                print(t_message)
                await self.action_handlers[t_message["action"]](t_message["id_task"], websocket,  *t_message["params"])
        finally:
            for c in self.connected_clients:
                c.close()

    async def auth(self, id_task, websocket, temp_id):
        #print("Возвращаем OK")
        await websocket.send(json.dumps({"id_task": id_task, "response" : "OK"}))
        #print("Вернули")


    async def start_server(self):
        async with websockets.serve(self.handler, "localhost", 8765):
            #print("Server started")
            await asyncio.Future()


if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())