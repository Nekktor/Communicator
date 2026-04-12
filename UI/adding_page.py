import customtkinter as ctk


class AddingPage(ctk.CTkFrame):
    def __init__(self, master, back_to_chats, on_chat_adding_submit):
        # Инициализируем как CTkFrame
        super().__init__(master, corner_radius=0)

        self.returning = back_to_chats
        self.submitting = on_chat_adding_submit

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

        self.setup_initial_view()

    def setup_initial_view(self):
        # Размещение элементов
        self.title_label.pack(pady=10)

        self.chat_type_label.pack(pady=(10, 0))
        self.chat_type_choose_menu.pack(pady=10)

        self.chat_name_label.pack(pady=(10, 0))
        self.chat_name_entry.pack(pady=10)

        self.participants_label.pack(pady=(10, 0))
        self.participants_entry.pack(pady=10)

        self.avatar_url_label.pack(pady=(10, 0))
        self.avatar_url_entry.pack(pady=(10, 0))

        # Кнопки прижимаем к нижней части окна
        self.back_button.place(relx=0.25, rely=0.9, anchor="center")
        self.submit_button.place(relx=0.75, rely=0.9, anchor="center")

    def show_adding_page(self):
        self.pack(expand=True, fill="both")

    def hide_adding_page(self):
        self.pack_forget()
