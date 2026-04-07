import customtkinter as ctk


class AddingPage(ctk.CTkFrame):
    def __init__(self, master, back_to_chats, on_chat_adding_submit):
        # Инициализируем как CTkFrame
        super().__init__(master)
        self.master = master
        self.returning = back_to_chats
        self.submitting = on_chat_adding_submit

        # Основной контейнер страницы
        self.adding_page = ctk.CTkFrame(self.master, corner_radius=15)

        # Заголовок страницы
        self.title_label = ctk.CTkLabel(
            self.adding_page,
            text="Создание нового чата",
            font=("Arial", 24, "bold")
        )

        # Поля для ввода с подсказками (placeholder)
        self.chat_name_label = ctk.CTkLabel(self.adding_page, text='Название чата:')
        self.chat_name_entry = ctk.CTkEntry(
            self.adding_page,
            width=400,
            height=40,
            placeholder_text="Например: Проект Альфа"
        )

        self.participants_label = ctk.CTkLabel(self.adding_page, text='Участники (через запятую):')
        self.participants_entry = ctk.CTkEntry(
            self.adding_page,
            width=400,
            height=40,
            placeholder_text="user1, user2, user3"
        )

        # Кнопки с использованием относительных координат для адаптивности
        self.back_button = ctk.CTkButton(
            self.adding_page,
            text="Вернуться к чатам",
            fg_color="transparent",
            border_width=2,
            width=200,
            height=45,
            command=self.returning
        )

        self.submit_button = ctk.CTkButton(
            self.adding_page,
            text="Создать чат",
            width=200,
            height=45,
            command=self.submitting
        )

        # Размещение элементов
        self.title_label.pack(pady=(40, 30))

        self.chat_name_label.pack(pady=(10, 0))
        self.chat_name_entry.pack(pady=10)

        self.participants_label.pack(pady=(20, 0))
        self.participants_entry.pack(pady=10)

        # Кнопки прижимаем к нижней части окна
        self.back_button.place(relx=0.25, rely=0.85, anchor="center")
        self.submit_button.place(relx=0.75, rely=0.85, anchor="center")

    def show_adding_page(self):
        self.adding_page.pack(expand=True, fill="both", padx=20, pady=20)

    def hide_adding_page(self):
        self.adding_page.pack_forget()
