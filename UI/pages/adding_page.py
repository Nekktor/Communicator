import customtkinter as ctk


class AddingPage(ctk.CTkFrame):
    def __init__(self, master, back_to_chats, on_chat_adding_submit):
        # Инициализируем как CTkFrame
        super().__init__(master, corner_radius=0)

        self.returning = back_to_chats
        self.submitting = on_chat_adding_submit

        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_rowconfigure((0, 11), weight=1)

        # Заголовок страницы
        self.title_label = ctk.CTkLabel(
            self,
            text="Создание нового чата",
            font=("Arial", 24, "bold")
        )

        self.chat_type_label = ctk.CTkLabel(
            self,
            text="Выберите тип чата:",
            font=("Arial", 14)
        )

        self.chat_type_choose_menu = ctk.CTkOptionMenu(
            self,
            width=300,
            height=50,
            values = ["Личная переписка", "Группа", "Канал"]
        )

        self.chat_name_label = ctk.CTkLabel(
            self,
            text='Название чата:',
            font=("Arial", 14)
        )

        self.chat_name_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="Например: Проект Альфа"
        )

        self.participants_label = ctk.CTkLabel(
            self,
            text='Участники:',
            font=("Arial", 14)
        )

        self.participants_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="user1, user2, user3"
        )

        self.avatar_url_label = ctk.CTkLabel(
            self,
            text="Ссылка на изображение:",
            font=("Arial", 14)
        )

        self.avatar_url_entry = ctk.CTkEntry(
            self,
            width=400,
            height=40,
            placeholder_text="Вставьте сюда ссылку на изображение для аватара чата"
        )

        # Кнопки с использованием относительных координат для адаптивности
        self.back_button = ctk.CTkButton(
            self,
            text="Вернуться к чатам",
            fg_color="transparent",
            border_width=2,
            width=200,
            height=45,
            command=self.returning
        )

        self.submit_button = ctk.CTkButton(
            self,
            text="Создать чат",
            width=200,
            height=45,
            command=self.submitting
        )

        self.error_label = ctk.CTkLabel(
            self,
            text='',
            text_color="red"
        )

        self.setup_initial_view()

    def setup_initial_view(self):
        # Все элементы размещаем в column=1 (центр)
        self.title_label.grid(row=0, column=1, columnspan=2, pady=(40, 20))

        self.chat_type_label.grid(row=1, column=1, columnspan=2, pady=(10, 0))
        self.chat_type_choose_menu.grid(row=2, columnspan=2, column=1, pady=10)

        self.chat_name_label.grid(row=3, column=1, columnspan=2, pady=(10, 0))
        self.chat_name_entry.grid(row=4, column=1, columnspan=2, pady=10)

        self.participants_label.grid(row=5, column=1, columnspan=2, pady=(10, 0))
        self.participants_entry.grid(row=6, column=1, columnspan=2, pady=10)

        self.avatar_url_label.grid(row=7, column=1, columnspan=2, pady=(10, 0))
        self.avatar_url_entry.grid(row=8, column=1, columnspan=2, pady=10)

        self.error_label.grid(row=9, column=1, columnspan=2, pady=10)

        self.back_button.grid(row=10, column=1, padx=(0, 10), pady=10, sticky="nsew")
        self.submit_button.grid(row=10, column=2, padx=(10, 0), pady=10, sticky="nsew")

    def error_callback(self, error):
        self.error_label.configure(text=error)

    def show_adding_page(self):
        self.pack(expand=True, fill="both")
        self.error_label.configure(text='')

    def hide_adding_page(self):
        self.pack_forget()
