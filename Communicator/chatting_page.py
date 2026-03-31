import tkinter as tk

class ChattingPage:
    _instance = None

    def __new__(cls, master, switch_to_adding_page):
        """
        Интерфэйс основного приложение, включает окна со списком чатов и с выбранным чатом

        :param master: Главное окно приложения, находится в main
        :param switch_to_adding_page: Метод, перемещающий пользователя на страницу для добавления нового чата
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, master, switch_to_adding_page):
        self.master = master
        self.switch_to_adding_chat = switch_to_adding_page

        # Поле с интерфэйсом списка чатов
        self.chats_list_frame = tk.Frame(self.master, height=600, width=300, bd=5, relief="solid")
        self.chats_list_frame.pack_propagate(False)

        self.chats_list_label = tk.Label(self.chats_list_frame, text="Чаты", bd=1, relief="solid")

        self.add_new_chat_button = tk.Button(self.chats_list_frame, text='Добавить новый чат', width=20, height=5, relief="solid", command=self.switch_to_adding_chat)

        # Поле с интерфэйсом выбранного чата
        self.chat_frame = tk.Frame(self.master, height=600, width=500, bd=5, relief="solid")
        self.chat_frame.pack_propagate(False)

        self.chat_label = tk.Label(self.chat_frame, text="Чат")

        # Размещение элементов на экране
        self.chat_label.pack(side="top")
        self.chats_list_label.pack(side="top", fill="x")
        self.add_new_chat_button.pack(side="top", pady=5)

    def show_chatting_page(self):
        self.chats_list_frame.pack(side="left")
        self.chat_frame.pack(side="right")

    def hide_chatting_page(self):
        self.chats_list_frame.pack_forget()
        self.chat_frame.pack_forget()