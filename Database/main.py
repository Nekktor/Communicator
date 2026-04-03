from Database.init import engine, Base, Session

# Инициализация классов таблиц и классов с методами
from Database.methods.users import UsersRequests
from Database.methods.chats import ChatsRequests
from Database.methods.messages import MessagesRequests
from Database.methods.participants import ParticipantsRequests

# Создание всех ещё не созданных таблиц (см. Database.methods.init)
# Base.metadata.create_all(engine)  # Модели с родительским классом Base записываются в Base.metadata

# Главный класс - через него осуществляется работа с методами
class DataBase:
    def __init__(self, session):
        self.users = UsersRequests(session)
        self.chats = ChatsRequests(session)
        self.messages = MessagesRequests(session)
        self.participants = ParticipantsRequests(session)