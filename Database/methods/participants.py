from typing import Any

from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from sqlalchemy import select, and_


# Sql-запросы у таблице participants
class ParticipantsRequests(BasicMethods[Participants]):
    def __init__(self, session: Session):
        super().__init__(session, Participants)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, chat_id: int, user_id: int, role: str = None):
        return super().add(chat_id=chat_id, user_id=user_id, role=role)

    # Чтобы были подсказки
    def delete(self, chat_id: int, user_id: int) -> dict:
        return super().delete([chat_id, user_id])

    # Чтобы были подсказки
    def update(self, attr_name: str, value: Any, chat_id, user_id) -> dict:
        return super().update(attr_name, value, chat_id, user_id)
