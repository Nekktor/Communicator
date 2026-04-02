from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from datetime import date


# Sql-запросы у таблице chats
class ChatsRequests(BasicMethods[Chats]):
    def __init__(self, session: Session):
        super().__init__(session, Chats)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, name: str, avatar_url: str = None):
        return super().add(name=name, avatar_url=avatar_url)

