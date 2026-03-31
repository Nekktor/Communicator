class User:
    _instance = None

    def __new__(cls, name, username):
        """
        if пользователь зарегистрирован, возвращает существующий класс
        elif пользователь не зарегистрирован
            if данные для регистрации верны, создаёт новый класс
            else не создаёт новый класс

        :param name: Отображаемое имя пользователя
        :param username: Уникальное имя пользователя в системе
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Переменные для регистрации (пока 2)
            cls._instance.name = name
            cls._instance.username = username

        return cls._instance


    def registration_check(self, username) -> bool:
        # Код для проверки уникальность
        pass

    def add_user(self, name, username) -> None:
        # Код для добавления данных пользователя в БД
        pass

    def login_check(self, username) -> bool:
        # Код для проверки на существования имени пользователя в БД
        pass

    def get_user_data(self, username) -> dict:
        # Код для получения данных пользователя
        # В формате словаря {'name': Имя, 'username': Имя пользователя}
        pass







