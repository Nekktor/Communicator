from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import date


# Sql-запросы у таблице chats
class ChatsRequests(BasicMethods[Chats]):
    def __init__(self, session: Session):
        super().__init__(session, Chats)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, name: str, avatar_url: str = None):
        return super().add(name=name, avatar_url=avatar_url)

    def select_all_chats_by_id_user(self, user_id):
        query = select(Chats).join(Chats.participants).where(Participants.user_id == user_id)
        q = self.session.execute(query).scalars().all()
        s = self.get_dict(q)
        print(3, s)



    # def dele(self):
    #
    #     from sqlalchemy import select
    #     from Database.models.chats import Chats
    #
    #     q = self.session.scalars(select(Chats)).all()
    #     print(q)
    #     from sqlalchemy import create_engine
    #     connection = ("postgresql://admin:bbqb5ON9TyrL7UwHbITyDT22ILByL0fU@dpg-d76in4hr0fns73cbkjk0-"
    #                   "a.oregon-postgres.render.com/main_database_4beq")  # Удалённая БД (render.com)
    #     # connection = "postgresql+psycopg2://postgres:Sokol_12@localhost:5432/postgres"  # Локальная БД
    #     engine = create_engine(connection)
    #
    #     from sqlalchemy import text
    #     with engine.connect() as conn:
    #         conn.execute(text('DROP TABLE IF EXISTS public.chats CASCADE'))
    #         conn.commit()
    #
    #     print(q)

