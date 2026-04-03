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

    # Переопределение метода delete
    def delete(self, chat_id: int, user_id: int) -> None:
        """
        Удаление строки с chat_id = chat_id и user_id = user_id
        """

        self.exists('chat_id', value=chat_id)  # Проверка на существование такого chat_id
        self.exists('user_id', value=user_id)  # Проверка на существование такого user_id
        participant = self.session.get(Participants, (chat_id, user_id))  # Получение участника группы
        self.session.delete(participant)  # Удаление участника

        print(f'Запись в таблице {self.model.__name__} с chat_id {chat_id} и user_id {user_id} удалёна')

    def update(self, chat_id: int, user_id: int, attr_name: str, value: Any) -> None:
        """
        Обновление у пользователя с chat_id = chat_id и user_id = user_id
            атрибута attr_name на значение value
        """

        self.exists('chat_id', value=chat_id)  # Проверка на существование такого chat_id
        self.exists('user_id', value=user_id)  # Проверка на существование такого user_id
        self._get_column(attr_name)  # Проверка существования такой колонки

        instance = self.session.get(self.model, [chat_id, user_id])
        setattr(instance, attr_name, value)
        print(f'Запись в таблице {self.model.__name__} '
              f'с id {id} и в колонке {attr_name} обновлена на {value}')

