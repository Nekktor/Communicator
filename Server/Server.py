import json

import websockets
import asyncio
#from Database.main import Session, DataBase
#from typing import Any
#from sqlalchemy import select, Column
#from Database.models.participants import UserRoleEnum
#from Database.models.messages import MessageTypeEnum
#from datetime import date
#
#from Database.methods.basic_methods import BasicMethods
#from test_database import *

class Server():
    def __init__(self):
        self.connected_clients = set()
        self.action_handlers = {
            "auth" : self.auth,
            "create_message" : self.create_message,
            "get_chats" : self.get_chats
        }

    async def handler(self, websocket):
        try:
            print("Подключено")
            async for message in websocket:
                t_message = json.loads(message)
                print(f"1 + {t_message}")
                await self.action_handlers[t_message["action"]](t_message["id_task"], websocket,  *t_message["params"])
        finally:
            for c in self.connected_clients:
                c.close()

    async def auth(self, id_task, websocket, username):
        #print("Возвращаем OK")
        try:
            out = username
            #out = db.users.exists("username", username) # здесь вызвать метода проверки возможности добавления пользователя с пааметрами name, username, lastname (они будут равны = ["Никита2", "Nikitka", "Соколов2"])
            await websocket.send(json.dumps({"id_task": id_task, "response": out}))
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send(json.dumps({"id_task": id_task, "response": "Fall"}))
        #await websocket.send(json.dumps({"id_task": id_task, "response" : "OK"}))
        #print("Вернули")

    async def create_message(self, id_task, websocket, username, content):
        try:
            #создание сообщения, добавлен е его в чат БД
            await websocket.send(json.dumps({"id_task": id_task, "response": "сообщение отправлено"}))
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send(json.dumps({"id_task": id_task, "response": "Fall"}))
    async def start_server(self):
        async with websockets.serve(self.handler, "localhost", 8765):
            print("Server started")
            await asyncio.Future()

    async def get_chats(self, id_task, websocket):
        try:
            chats = {}#чаты из БД
            await websocket.send(json.dumps({"id_task": id_task, "response" : chats}))
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send(json.dumps({"id_task": id_task, "response": "Fall"}))
"""with Session() as session:
    db = DataBase(session)
    try:
        with session.begin():  # ← одна транзакция на всё
                # РАБОЧАЯ ЧАСТЬ
                if __name__ == "__main__":
                    server = Server()
                    asyncio.run(server.start_server())
                #health_check_users(db)
                #health_check_chats(db)
                #health_check_participants(db)
                #health_check_messages(db)

    except Exception as e:
        print(f"Ошибка: {e}")"""

if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())