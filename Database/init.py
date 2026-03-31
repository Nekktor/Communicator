"""
Файл, где инициализируется вся логика работы с БД
"""

# Убрать комментарии в Database.init на 11 строчке в зависимости наличия postgresql.
# Убрать комментарии в Database.models.user на 17 строчке в зависимости наличия postgresql.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:Sokol_12@localhost:5432/postgres")  # Если есть postgresql
# engine = create_engine("sqlite:///mydb.db")  # Если нет postgresql
Base = declarative_base()
Session = sessionmaker(bind=engine)