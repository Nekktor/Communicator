import tkinter as tk

class SignUpPage:
    _instance = None

    def __new__(cls, master, register_method, login_method):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.master = master
            cls._instance.is_user_registered = False
            cls._instance.register = register_method
            cls._instance.login = login_method

            # Рамка на которой размещены элементы окна
            cls._instance.sign_up_page = tk.Frame(cls._instance.master, bd=5, relief='solid')

            # Подпись к окну
            cls._instance.process_label = tk.Label(cls._instance.sign_up_page, font=("Arial", 20), text='Создание аккаунта')

            # Подписи к полям ввода
            cls._instance.name_entry_label = tk.Label(cls._instance.sign_up_page, text='Введите своё имя')
            cls._instance.username_entry_label = tk.Label(cls._instance.sign_up_page, text='Введите имя пользователя')

            # Поля ввода имени и имени пользователя
            cls._instance.name_entry = tk.Entry(cls._instance.sign_up_page, font=("Arial", 12))
            cls._instance.username_entry = tk.Entry(cls._instance.sign_up_page, font=("Arial", 12))

            # Кнопка подтверждения введённых данных
            cls._instance.submit_button = tk.Button(cls._instance.sign_up_page, text="Подтвердить", width=25, height=3, command=cls._instance.register)

            # Кнопки для смены производимого действия
            cls._instance.login_button = tk.Button(cls._instance.sign_up_page, text="Войти в аккаунт", width=25, height=3, command=cls._instance.show_login_interface)
            cls._instance.register_button = tk.Button(cls._instance.sign_up_page, text="Зарегистрироваться", width=25, height=3, command=cls._instance.show_register_interface)

            # Надпись для показа ошибок
            cls._instance.error_label = tk.Label(cls._instance.sign_up_page, font=("Arial", 12), fg='red')

            # Размещение элементов на экране
            cls._instance.process_label.pack(side='top', pady=20)

            cls._instance.name_entry_label.pack(side='top', pady=20)
            cls._instance.name_entry.pack(side="top", pady=10)
            cls._instance.username_entry_label.pack(side='top', pady=10)
            cls._instance.username_entry.pack(side='top', pady=10)

            cls._instance.submit_button.place(x=500, y=500)
            cls._instance.login_button.place(x=100, y=500)

        return cls._instance

    def error_callback(self, error):
        self.error_label.config(text=error)
        self.error_label.pack(side='bottom', pady=10)

    def show_login_interface(self):
        # Скрываем поле для ввода имени
        self.name_entry_label.pack_forget()
        self.name_entry.pack_forget()

        # Заменяем кнопку для переключения операций
        self.login_button.place_forget()
        self.register_button.place(x=100, y=500)

        # Выводим для пользователя название текущей операции
        self.process_label.config(text='Вход в аккаунт')

        # Изменяем функцию кнопки подтверждения на авторизацию
        self.submit_button.config(command=self.login)

    def show_register_interface(self):
        # Убираем старое поле ввода имени пользователя, т.к. оно нарушит порядок
        self.username_entry_label.pack_forget()
        self.username_entry.pack_forget()

        # Выстраиваем UI для регистрации
        self.name_entry_label.pack(side='top', pady=20)
        self.name_entry.pack(side="top", pady=10)
        self.username_entry_label.pack(side='top', pady=10)
        self.username_entry.pack(side='top', pady=10)

        # Заменяем кнопку для переключения операций
        self.register_button.place_forget()
        self.login_button.place(x=100, y=500)

        # Выводим для пользователя название текущей операции
        self.process_label.config(text='Создание аккаунта')

        # Изменяем функцию кнопки подтверждения на регистрацию
        self.submit_button.config(command=self.register)

    def show_sign_up_page(self):
        self.sign_up_page.pack(fill='both', expand=True)

    def hide_sign_up_page(self):
        self.sign_up_page.pack_forget()
