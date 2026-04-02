"""
Здесь собраны основные методы для всех таблиц
"""

from typing import Generic, TypeVar, Sequence, Any
from sqlalchemy import select, Column
from sqlalchemy.orm import Session

from Database.models.users import Users

T = TypeVar("T")  # Нужно для правильной аннотации и подсказок

class BasicMethods(Generic[T]):
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    @staticmethod
    def __get_attributes(obj) -> dict:
        attrs = {}

        # перебор через dir() и getattr, пропуская исключения и приватные, если нужно
        for name in dir(obj):
            if name.startswith('_'):
                continue
            attrs[name] = getattr(obj, name)
        return attrs

    def _get_column(self, attr_name: str) -> Column | AttributeError:
        """
        Проверка существования колонки в таблице

        :param attr_name: колонка, существование которой надо проверить
        :return: колонка таблицы
        """

        if not hasattr(self.model, attr_name):
            raise AttributeError(f"Модель {self.model.__name__} не содержит поля '{attr_name}'")
        return getattr(self.model, attr_name)

    def _exists(self, attr_name: str, value: Any) -> None | ValueError:
        """
        Проверка существования у колонки attr_name значения value

        :param attr_name: название колонки
        :param value: значение колонки
        :return: булевое значение
        """

        column = self._get_column(attr_name)
        is_not_exits = self.session.execute(select(self.model).where(column == value)).scalar() is None
        if is_not_exits: raise ValueError(f"{attr_name} - несуществующие в таблице {self.model.__name__} колонка")

    def get_dict(self, raw_users: Sequence[list]) -> list[dict]:
        structured_users = list()
        for user in raw_users:
            user_dict = self.__get_attributes(user)
            for key, value in user_dict.copy().items():  # Проверка элементов на экземпляр класса
                # Если не объект класса "sqlalchemy" или список, то возращаем
                type_attr = getattr(value, '__module__', '')
                if type_attr.startswith('sqlalchemy.') or type_attr.startswith('Database.'):
                    # Если нужны связанные строки из других таблиц -
                    # and not isinstance(value, InstrumentedList)
                    del user_dict[key]  # Удаление неподходящих атрибутов

            structured_users.append(user_dict)

        return structured_users

    def add(self, **kwargs) -> None:
        """
        Добавление пользователя в таблицу

        :param kwargs:
        :return:
        """

        self.session.add(self.model(**kwargs))
        print(f'Запись в таблице {self.model.__name__} добавлена с параметрами {kwargs}')

    def select_all(self) -> list[dict]:
        """
        Вывод все значения всех пользователей
        :return: список классов таблицы
        """

        raw_users = self.session.scalars(select(self.model)).all()
        structured_users = self.get_dict(raw_users)

        return structured_users

    def update(self, id: int, attr_name: str, value: Any) -> None:
        """
        Обновление у пользователя с id = id атрибута attr_name на значение value
        """

        self._exists('id', value=id)  # Проверка существования такого id
        self._get_column(attr_name)  # Проверка существования такой колонки

        instance = self.session.get(self.model, id)
        setattr(instance, attr_name, value)
        print(f'Запись в таблице {self.model.__name__} '
              f'с id {id} и в колонке {attr_name} обновлена на {value}')

    def delete(self, id: int) -> None:
        """
        Удаление записи с id = id
        """

        self._exists('id', value=id)  # Проверка на существование такого id
        self.session.delete(self.session.get(self.model, id))
        print(f'Запись в таблице {self.model.__name__} с id {id} удалёна')
