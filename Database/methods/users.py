from Database.methods.basic_methods import BasicMethods
from Database.methods.init import *
from sqlalchemy.orm import Session
from datetime import date


# Sql-запросы у таблице users
class UsersRequests(BasicMethods[Users]):
    def __init__(self, session: Session):
        super().__init__(session, Users)  # Инициализация базовых четырёх методов

    # Чтобы были подсказки
    def add(self, name: str, username: str, lastname: str = None, birthday: str = date,
            avatar_url: str = None, phone: str | int = None, email: str = None):
        return super().add(name=name, username=username, lastname=lastname, birthday=birthday,
                           avatar_url=avatar_url, phone=phone, email=email)