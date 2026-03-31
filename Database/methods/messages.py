from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from datetime import date


# Sql-запросы у таблице messages
class MessagesRequests(BasicMethods[Messages]):
    def __init__(self, session: Session):
        super().__init__(session, Messages)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, chat_id: int, user_id: int, type: str = None, text: str = None, file_id: int = None):
        return super().add(type=type, text=text, file_id=file_id, chat_id=chat_id, user_id=user_id)
