import customtkinter as ctk

from start_page import StartPage
from chatting_page import ChattingPage
from adding_page import AddingPage
from sign_up_page import SignUpPage
from chat_view import MessageView, ChatView
from selectable_chat_view import SelectableChatView

# Настройка внешнего вида (можно вынести в initialize)
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("800x600")
        self.root.title("Communicator")

        # Инициализация классов страниц
        self.start_page = StartPage(self.root)
        self.chatting_page = ChattingPage(self.root, self.switch_to_adding_page)
        self.adding_page = AddingPage(self.root, self.switch_to_chatting_page, self.on_chat_adding_submit)
        self.sign_up_page = SignUpPage(self.root, self.register_user, self.login_user)

        self.available_chats = []
        self.current_page = 'start_page'
        self.current_chat = None

    def remove_pages(self) -> None:
        self.start_page.hide_start_page()
        self.adding_page.hide_adding_page()
        self.chatting_page.hide_chatting_page()
        self.sign_up_page.hide_sign_up_page()

    def switch_to_chatting_page(self) -> None:
        self.remove_pages()
        self.chatting_page.show_chatting_page()
        self.current_page = 'chatting_page'

    def switch_to_sign_up_page(self) -> None:
        self.remove_pages()
        self.sign_up_page.show_sign_up_page()
        self.current_page = 'sign_up_page'

    def switch_to_adding_page(self) -> None:
        self.remove_pages()
        self.adding_page.show_adding_page()
        self.current_page = 'adding_page'

    def get_current_page(self) -> str:
        return self.current_page

    #################################################################################################
    # Методы обработчики добавления новых элементов UI
    #################################################################################################

    # Метод для добавления чата
    def on_chat_adding_submit(self) -> None:
        chat_type = self.adding_page.chat_type_choose_menu.get()
        chat_name = self.adding_page.chat_name_entry.get()
        participants = self.adding_page.participants_entry.get().split(',')
        participants_count = len(participants)
        last_message = ''
        avatar_url = self.adding_page.avatar_url_entry.get()

        self.add_selectable_chat_view(avatar_url, chat_name, last_message)
        self.switch_to_chatting_page()

    # Метод для отправки сообщения
    def send_message(self) -> None:
        message_text = self.current_chat.message_entry.get()
        if message_text != '':
            self.add_message_view('text', message_text, 'User')
            self.current_chat.message_entry.delete(0, 'end')

    # Метод для открытия чата
    def open_chat(self, chat_id=None) -> None:
        """
        Получаем информацию о чате из БД и передаём её

        :param chat_id: ID открываемого чата
        """
        self.add_chat_view("group", "Разработка немыслимого", 3)

#################################################################################################
    # Методы добавление UI
#################################################################################################

    # Добавление вида выбранного чата
    def add_chat_view(self, chat_type, name, participants_count):
        self.current_chat = ChatView(self.chatting_page, chat_type, name, participants_count, './no_image.jpg', self.send_message)
        self.chatting_page.on_chat_selection()
        self.current_chat.grid(column=1, row=0, sticky="nsew")

    # Добавление вида чата на панели списка чатов
    def add_selectable_chat_view(self, avatar_url: str, name: str, last_message: str) -> None:
        selectable_chat = SelectableChatView(self.chatting_page.chats_list_scrollable_frame, avatar_url, name, last_message)
        selectable_chat.bind("<Button-1>", command=self.open_chat)
        self.available_chats.append(name)
        selectable_chat.pack(side='top', anchor='ne', pady=5, padx=5, fill="x")

    # Добавление вида сообщения
    def add_message_view(self, content_type: str, content: str, sender_name: str) -> None:
        if sender_name == 'User':
            message = MessageView(self.current_chat.messages_frame, content_type, content, sender_name)
            message.pack(side='bottom', anchor='se', pady=5, padx=5, expand=True)
        else:
            # Ищем имя по id отправителя и передаём его
            pass

    #################################################################################################
    # Функции для авторизации
    #################################################################################################

    def register_user(self) -> None:
        user_name = self.sign_up_page.name_entry.get()
        user_username = self.sign_up_page.username_entry.get()
        self.switch_to_chatting_page()

    def login_user(self) -> None:
        user_username = self.sign_up_page.username_entry.get()
        self.switch_to_chatting_page()

    def sign_up_error_callback(self, error: str):
        self.sign_up_page.error_callback(error)

    def initialize(self):
        self.start_page.show_start_page()
        self.root.after(2000, self.switch_to_sign_up_page)

    def run(self):
        self.initialize()
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
