from Database.methods.init import *
from Database.init import Session
from sqlalchemy.orm import Session
from sqlalchemy import select



# Sql-запросы у таблице users
class UsersRequests:
    def __init__(self, session: Session):
        self.session = session

    def _check_unique_attr(self, attr_name: str, value: str) -> bool:
        """
        Проверка: содержит ли field_name значение value в таблице Users?
        :param attr_name: название колонки
        :param value: значение колонки
        :return: True если найден, иначе False
        """

        if value == None: return False  # Возращает True, если значение равно None (так надо)

        # Проверка на содержание field_name в таблице Users
        column = getattr(Users, attr_name)  # >>> Users.field_name
        if not column:
            print(f"Модель Users не содержит поля '{attr_name}'")

        return self.session.execute(
            select(Users).where(column == value)).scalar() is not None  # True, если уже существует

    def add(self, name: str, username: str, lastname: str = None, birthday = None,
                 avatar_url: str = None, phone: str = None, email: str = None) -> None:
        """
        Добавляет пользователя в таблицу или выводит ошибку
        """

        isUsernameBe = self._check_unique_attr('username', value=username)
        isPhoneBe = self._check_unique_attr('phone', value=phone)
        isEmailBe = self._check_unique_attr('email', value=email)
        if not any([isUsernameBe, isPhoneBe, isEmailBe]):
            self.session.add(
                Users(name=name, username=username, lastname=lastname, birthday=birthday,
                         avatar_url=avatar_url, phone=phone, email=email))
            print(f'Пользователь {name} добавлен')
        else:
            print('Такой username, телефон или почта занята. Попробуйте другую')

    def select_all(self):
        """
        Выводит все значения всех пользователей
        :return: список классов Users
        """
        return self.session.execute(select(Users)).scalars().all()

    def update(self, id: int, attr_name: str, value: str) -> None:
        """
        Обновляет у пользователя с id = id атрибут attr_name на value
        """

        isIdBe = self._check_unique_attr('id', value=str(id))
        if isIdBe:
            if not hasattr(Users, attr_name):  # Проверка на существования attr_name в Users
                raise ValueError(f"Request.user.update: Модель Users не содержит поля '{attr_name}'")
            # Изменение значения Users.attr_name = value
            setattr(self.session.get(Users, id), attr_name, value)
            print(f'Пользователь с id = {id} обновлён')
        else:
            print(f'Request.user.update: {id} - несуществующие в таблице id')

    def delete(self, id: int) -> None:
        """
        Удаляет пользователя с id = id
        """
        isAttrBe = self._check_unique_attr('id', value=id)
        if isAttrBe:
            self.session.delete(self.session.get(Users, id))
            print(f'Пользователь с id {id} удалён')
        else:
            print(f'Request.user.delete: {id} - несуществующие в таблице id')
