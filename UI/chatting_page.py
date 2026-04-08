import customtkinter as ctk


class ChattingPage(ctk.CTkFrame):
    def __init__(self, master, switch_to_adding_page, send_message):
        """
        Класс вмещающий в себя окно со списком чатов и выбранным чатом.

        :param master: Главное окно (ctk.Ctk) приложения в main
        :param switch_to_adding_page: Метод для перехода в окно добавления нового чата в main
        """
        super().__init__(master, corner_radius=0)

        self.switch_to_adding_chat = switch_to_adding_page
        self.send_message = send_message

######### --- Левая панель: список чатов --- #########

        # Рамка для размещения списка чатов
        self.chats_list_frame = ctk.CTkFrame(
            self,
            width=300,
            corner_radius=0,
            border_width=1,
            border_color="gray"
        )
        self.chats_list_frame.pack_propagate(False)

        # Область для самого списка чатов
        self.chats_list_scrollable_frame = ctk.CTkScrollableFrame(
            self.chats_list_frame,
            border_width=1
        )

        # Кнопка добавления нового чата
        self.add_new_chat_button = ctk.CTkButton(
            self.chats_list_frame,
            height=40,
            text='Добавить новый чат',
            command=self.switch_to_adding_chat
        )

######### --- Правая панель: окно чата --- #########

        # Рамка для выбранного чата
        self.chat_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            border_width=1,
            border_color="gray"
        )

        # Поле для ввода сообщения на отправку
        self.message_entry = ctk.CTkEntry(
            self.chat_frame,
            height=40,
            width=440,
            placeholder_text='Введите своё сообщение'
        )
        self.message_entry.pack_propagate(False)

        self.send_button = ctk.CTkButton(
            self.chat_frame,
            height=40,
            width=40,
            text='',
            corner_radius=20,
            command=self.send_message
        )
        self.send_button.pack_propagate(False)

        self.setup_initial_view()

    def setup_initial_view(self):
        # Упаковка рамки со списком чатов
        self.chats_list_frame.pack(side="left", fill="y")

        self.chats_list_scrollable_frame.pack(side="top", pady=10, padx=5, fill="both", expand=True)
        self.add_new_chat_button.pack(side="bottom", pady=5, padx=5, fill="x")

        # Упаковка выбранного чата
        self.chat_frame.pack(side="right", fill="both", expand=True)

        self.message_entry.pack(side="left", anchor="sw", pady=5, padx=5)
        self.send_button.pack(side="right", anchor="se", pady=5, padx=5)

    def show_chatting_page(self):
        self.pack(fill="both", expand=True)

    def hide_chatting_page(self):
        self.pack_forget()
