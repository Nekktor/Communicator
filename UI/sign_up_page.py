import customtkinter as ctk

class SignUpPage(ctk.CTkFrame):
    def __init__(self, master, register_method, login_method):
        # Инициализируем сам класс как CTkFrame
        super().__init__(master, corner_radius=15)

        self.register = register_method
        self.login = login_method

        # Заголовок
        self.process_label = ctk.CTkLabel(
            self,
            font=("Arial", 24, "bold"),
            text='Создание аккаунта'
        )

        # Поля ввода и подписи (master теперь self)
        self.name_entry_label = ctk.CTkLabel(self, text='Введите своё имя')
        self.name_entry = ctk.CTkEntry(self, width=300, height=40)

        self.username_entry_label = ctk.CTkLabel(self, text='Введите имя пользователя')
        self.username_entry = ctk.CTkEntry(self, width=300, height=40)

        # Кнопки
        self.submit_button = ctk.CTkButton(
            self,
            text="Подтвердить",
            width=200, height=45,
            command=self.register
        )

        self.login_button = ctk.CTkButton(
            self,
            text="Войти в аккаунт",
            fg_color="transparent", border_width=2,
            command=self.show_login_interface
        )

        self.register_button = ctk.CTkButton(
            self,
            text="Зарегистрироваться",
            fg_color="transparent", border_width=2,
            command=self.show_register_interface
        )

        # Надпись для ошибок
        self.error_label = ctk.CTkLabel(self, text='', text_color="red")

        # Начальное размещение элементов
        self.setup_initial_view()

    def setup_initial_view(self):
        self.process_label.pack(pady=(40, 20))
        self.name_entry_label.pack(pady=(10, 0))
        self.name_entry.pack(pady=10)
        self.username_entry_label.pack(pady=(10, 0))
        self.username_entry.pack(pady=10)

        self.login_button.place(relx=0.2, rely=0.85, anchor="center")
        self.submit_button.place(relx=0.7, rely=0.85, anchor="center")

    def error_callback(self, error):
        self.error_label.configure(text=error)
        self.error_label.pack(side='bottom', pady=20)

    def show_login_interface(self):
        self.name_entry_label.pack_forget()
        self.name_entry.pack_forget()

        self.login_button.place_forget()
        self.register_button.place(relx=0.2, rely=0.85, anchor="center")

        self.process_label.configure(text='Вход в аккаунт')
        self.submit_button.configure(command=self.login)

    def show_register_interface(self):
        self.username_entry_label.pack_forget()
        self.username_entry.pack_forget()

        self.name_entry_label.pack(pady=(10, 0))
        self.name_entry.pack(pady=10)
        self.username_entry_label.pack(pady=(10, 0))
        self.username_entry.pack(pady=10)

        self.register_button.place_forget()
        self.login_button.place(relx=0.2, rely=0.85, anchor="center")

        self.process_label.configure(text='Создание аккаунта')
        self.submit_button.configure(command=self.register)

    def show_sign_up_page(self):
        self.pack(fill='both', expand=True, padx=20, pady=20)

    def hide_sign_up_page(self):
        self.pack_forget()
