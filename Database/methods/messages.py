from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from sqlalchemy import select


# Sql-запросы у таблице messages
class MessagesRequests(BasicMethods[Messages]):
    def __init__(self, session: Session):
        super().__init__(session, Messages)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, chat_id: int, user_id: int, type: str = None, text: str = None, file_id: int = None):
        return super().add(type=type, text=text, file_id=file_id, chat_id=chat_id, user_id=user_id)

    def select_all_messages_by_chat_id(self, chat_id: int) -> dict:
        """
        Получение всех сообщений, которые написаны в чате с chat_id = chat_id

        :param chat_id: id чата
        :return: словарь, где isSuccess = True, если ошибок нет, иначе False.
        В data храниться список словарей с инфо об пользователях
        """

        query = select(Messages).where(Messages.chat_id == chat_id)
        raw_data = self.session.execute(query).scalars().all()
        structured_data = self._get_dict(raw_data)
        return {'isSuccess': True, 'data': structured_data}
