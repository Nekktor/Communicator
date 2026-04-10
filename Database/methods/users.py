from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import date


# Sql-запросы у таблице users
class UsersRequests(BasicMethods[Users]):
    def __init__(self, session: Session):
        super().__init__(session, Users)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, name: str, username: str, password: str, lastname: str = None, birthday: str = date.today(),
            avatar_url: str = None, phone: str | int = None, email: str = None):
        return super().add(name=name, username=username, lastname=lastname, birthday=birthday,
                           avatar_url=avatar_url, phone=phone, email=email, password=password)

    def select_all_users_by_chat_id(self, chat_id: int) -> dict:
        """
        Получение всех пользователей, которые состоят в чате с chat_id = chat_id

        :param chat_id: id чата
        :return: словарь, где isSuccess = True, если ошибок нет, иначе False.
        В data храниться список словарей с инфо об пользователях
        """

        query = select(Users).join(Users.participants).where(Participants.chat_id == chat_id)
        raw_data = self.session.execute(query).scalars().all()
        structured_data = self._get_dict(raw_data)
        return {'isSuccess': True, 'data': structured_data}

    def select_by_username(self, username: str) -> dict:
        data = self.session.execute(select(Users.id, Users.name).where(Users.username == username)).mappings().one_or_none()
        return {'isSuccess': True, 'data': dict(data)}

    def select_name_by_id(self, id: int) -> dict:
        data = self.session.execute(select(Users.name).where(Users.id == id)).mappings().one_or_none()
        return {'isSuccess': True, 'data': dict(data)}