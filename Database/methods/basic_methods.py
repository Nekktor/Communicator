"""
Здесь собраны основные методы для всех таблиц
"""

from typing import Generic, TypeVar, Sequence, Any
from sqlalchemy import select, Column
from sqlalchemy.orm import Session

T = TypeVar("T")  # Нужно для правильной аннотации и подсказок

class BasicMethods(Generic[T]):
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model


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

    def exists(self, attr_name: str, value: Any) -> bool:
        """
        Проверка существования у колонки attr_name значения value

        :param attr_name: название колонки
        :param value: значение колонки
        :return: булевое значение
        """

        column = self._get_column(attr_name)
        if not column: return False
        is_not_exits = self.session.execute(select(self.model).where(column == value)).scalar() is None
        # if is_not_exits: raise ValueError(f"{attr_name} - несуществующие в таблице {self.model.__name__} колонка")
        if is_not_exits: return False
        return True

    def add(self, **kwargs) -> None:
        """
        Добавление пользователя в таблицу

        :param kwargs:
        :return:
        """

        self.session.add(self.model(**kwargs))
        print(f'Запись в таблице {self.model.__name__} добавлена с параметрами {kwargs}')

    def select_all(self) -> Sequence[T]:
        """
        Вывод все значения всех пользователей
        :return: список классов таблицы
        """

        return self.session.scalars(select(self.model)).all()

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
