'''"""
Файл, где инициализируется вся логика работы с БД
"""

# Импорт библиотек для всей папки
from sqlalchemy import (Column, String, Integer, Date, Text, func, create_engine, select,
                        DateTime, ForeignKey, text)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from enum import Enum
from sqlalchemy.types import Enum as SQLEnum

# Создание базовых объектов
engine = create_engine("postgresql+psycopg2://postgres:Sokol_12@localhost:5432/postgres", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Создание классов таблиц и классов с методами
from Database.users import *
from Database.chats import *
from Database.messages import *
from Database.participants import *

# Создание всех ещё не созданных таблиц
Base.metadata.create_all(engine)

# Главный класс - через него осуществляется работа с методами
class Requests:
    def __init__(self, session):
        self.users = UsersRequests(session)
        self.chats = ChatsRequests(session)
        self.messages = MessagesRequests(session)
        self.participants = ParticipantsRequests(session)'''

# Убрать комментарии в Database.init на 40 строчке в зависимости наличия postgresql.
# Убрать комментарии в Database.models.user на 17 строчке в зависимости наличия postgresql.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# engine = create_engine("postgresql+psycopg2://postgres:Sokol_12@localhost:5432/postgres")  # Если есть postgresql
engine = create_engine("sqlite:///mydb.db")  # Если нет postgresql
Base = declarative_base()
Session = sessionmaker(bind=engine)