class Connection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Единоразовый вызов метода подключения к БД
            cls._instance._connect_database()

            # Переменные для взаимодействия с базой данных

        return cls._instance

    def _connect_database(self):
        # Метод подключения базы данных
        pass
