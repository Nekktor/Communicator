from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from Database.init import catching_errors
from sqlalchemy.orm import Session
from sqlalchemy import select



# Sql-запросы у таблице chats
class ChatsRequests(BasicMethods[Chats]):
    def __init__(self, session: Session):
        super().__init__(session, Chats)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, name: str, avatar_url: str = None):
        return super().add(name=name, avatar_url=avatar_url)

    @catching_errors()
    def select_all_chats_by_id_user(self, user_id: int) -> dict:
        """
        Получение всех чатов, в которых состоит пользователь с id = user_id

        :param user_id: id нужного пользователя
        :return: Список словарей, где словарь - данные о чате
        """

        query = select(Chats).join(Chats.participants).where(Participants.user_id == user_id)
        raw_data = self.session.execute(query).scalars().all()
        structured_data = self._get_dict(raw_data)
        return {'isSuccess': True, 'data': structured_data}

