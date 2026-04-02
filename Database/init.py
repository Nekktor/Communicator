"""
Файл, где инициализируется вся логика работы с БД
"""

# Убрать комментарии в Database.init на 11 строчке в зависимости наличия postgresql.
# Убрать комментарии в Database.models.user на 17 строчке в зависимости наличия postgresql.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


connection = ("postgresql://admin:bbqb5ON9TyrL7UwHbITyDT22ILByL0fU@dpg-d76in4hr0fns73cbkjk0-"
              "a.oregon-postgres.render.com/main_database_4beq")  # Удалённая БД (render.com)
# connection = "postgresql+psycopg2://postgres:Sokol_12@localhost:5432/postgres"  # Локальная БД
engine = create_engine(connection)
Base = declarative_base()
Session = sessionmaker(bind=engine)

"""
# Удаление всех таблиц. :)
from sqlalchemy import MetaData
metadata = MetaData()
metadata.reflect(bind=engine)        # загрузить существующие таблицы
metadata.drop_all(bind=engine)      # удалить все отражённые таблицы
"""