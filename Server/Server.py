import json

import websockets
import asyncio
from Database.main import Session, DataBase
from typing import Any
from sqlalchemy import select, Column
from Database.models.participants import UserRoleEnum
from Database.models.messages import MessageTypeEnum
from datetime import date

from Database.methods.basic_methods import BasicMethods


class Server():
    def __init__(self):
        self.connected_clients = set()
        self.action_handlers = {
            "auth" : self.auth
        }

    async def handler(self, websocket):
        try:
            print("Подключено")
            async for message in websocket:
                t_message = json.loads(message)
                print(t_message)
                await self.action_handlers[t_message["action"]](t_message["id_task"], websocket,  *t_message["params"])
        finally:
            for c in self.connected_clients:
                c.close()

    async def auth(self, id_task, websocket, username, ):
        #print("Возвращаем OK")
        try:

            out = basic_methods.BasicMethods.exists("username", username) # здесь вызвать метода проверки возможности добавления пользователя с пааметрами name, username, lastname (они будут равны = ["Никита2", "Nikitka", "Соколов2"])
            await websocket.send(json.dumps({"id_task": id_task, "response": out}))
        except Exception as e:
            print(e)
            await websocket.send(json.dumps({"id_task": id_task, "response": "Fall"}))
        #await websocket.send(json.dumps({"id_task": id_task, "response" : "OK"}))
        #print("Вернули")


    async def start_server(self):
        async with websockets.serve(self.handler, "localhost", 8765):
            #print("Server started")
            await asyncio.Future()


with Session() as session:
    db = DataBase(session)
    # try:
    with session.begin():  # ← одна транзакция на всё
            # РАБОЧАЯ ЧАСТЬ
            print("БД запущена")
            if __name__ == "__main__":
                server = Server()
                print("Сервер запущен")
                asyncio.run(server.start_server())
            #health_check_users(db)
            #health_check_chats(db)
            #health_check_participants(db)
            #health_check_messages(db)

    # except Exception as e:
    #     print(f"Ошибка: {e}")

"""if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())"""