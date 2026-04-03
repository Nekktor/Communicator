import json

import websockets
import asyncio
from Database.main import Session, DataBase
from Database.models.participants import UserRoleEnum
from Database.models.messages import MessageTypeEnum
from datetime import date


async def health_check_users(db, name, username, lastname, birthday="None", avatar_url="Nondfde", phone="83672443", email="43834834"):
    def views():
        print('-' * 150)

        users = db.users.select_all()
        for u in users:
            print(u.id, u.name, u.username, u.lastname, u.birthday, u.avatar_url,
                  u.date_created, u.last_time_online, u.phone, u.email, u.participants, u.chats, u.messages)

        print('-' * 150)

    #views()

    db.users.add(name=name, username=username, lastname=lastname,
                birthday=birthday, phone=phone, email=email)
    # db.users.add(name='Сева', username='Seva', lastname=None, birthday=None, phone='89876543210', email=None)
    # db.users.add(name='Юра', username='Yura', lastname='Мельник', birthday=None, phone=None, email=None)
    # db.users.add(name='Юра2', username='Yura2', lastname='Мельник',
    #              birthday=date(2011, 7, 14), phone=None, email=None)
    # views()

    # db.users.update(13, 'name', 'Юрчик')
    # views()

    # db.users.delete(14)
    # views()


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

    async def auth(self, id_task, websocket, name, username, lastname):
        #print("Возвращаем OK")
        try:
            await health_check_users(db, name, username, lastname, ) # здесь вызвать метода проверки возможности добавления пользователя с пааметрами name, username, lastname (они будут равны = ["Никита2", "Nikitka", "Соколов2"])
            await websocket.send(json.dumps({"id_task": id_task, "response": username}))
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
            if __name__ == "__main__":
                server = Server()
                asyncio.run(server.start_server())
            #health_check_users(db)
            #health_check_chats(db)
            #health_check_participants(db)
            #health_check_messages(db)

    # except Exception as e:
    #     print(f"Ошибка: {e}")

if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())