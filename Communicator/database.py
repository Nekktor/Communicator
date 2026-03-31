# Класс для доработки под используемую базу данных и написание методов взаимодействия с ней
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance._connect_database()
        return cls._instance

    def _connect_database(self):
        # Код для подключения к базе данных
        pass