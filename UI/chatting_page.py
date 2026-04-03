import tkinter as tk

class ChattingPage:
    _instance = None

    def __new__(cls, master, switch_to_adding_page):
        """
        UI основного приложение, включает окна со списком чатов и с выбранным чатом

        :param master: Главное окно приложения, находится в main
        :param switch_to_adding_page: Метод, перемещающий пользователя на страницу для добавления нового чата
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.master = master
            cls._instance.switch_to_adding_chat = switch_to_adding_page

            # Поле с UI списка чатов
            cls._instance.chats_list_frame = tk.Frame(cls._instance.master, height=600, width=300, bd=5, relief="solid")
            cls._instance.chats_list_frame.pack_propagate(False)

            cls._instance.chats_list_label = tk.Label(cls._instance.chats_list_frame, text="Чаты", bd=1, relief="solid")

            cls._instance.add_new_chat_button = tk.Button(cls._instance.chats_list_frame, text='Добавить новый чат', width=20, height=5,
                                                 relief="solid", command=cls._instance.switch_to_adding_chat)

            # Поле с UI выбранного чата
            cls._instance.chat_frame = tk.Frame(cls._instance.master, height=600, width=500, bd=5, relief="solid")
            cls._instance.chat_frame.pack_propagate(False)

            cls._instance.chat_label = tk.Label(cls._instance.chat_frame, text="Чат")

            # Размещение элементов на экране
            cls._instance.chat_label.pack(side="top")
            cls._instance.chats_list_label.pack(side="top", fill="x")
            cls._instance.add_new_chat_button.pack(side="top", pady=5)

        return cls._instance

    def show_chatting_page(self):
        self.chats_list_frame.pack(side="left")
        self.chat_frame.pack(side="right")

    def hide_chatting_page(self):
        self.chats_list_frame.pack_forget()
        self.chat_frame.pack_forget()