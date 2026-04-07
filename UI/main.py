import customtkinter as ctk

from start_page import StartPage
from chatting_page import ChattingPage
from adding_page import AddingPage
from sign_up_page import SignUpPage
from message_view import MessageView
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

        self.current_page = 'start_page'

        self.add_chat_view(None, "WOW")

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

    def on_chat_adding_submit(self) -> None:
        chat_name = self.adding_page.chat_name_entry.get()
        participants = self.adding_page.participants_entry.get().split(',')
        print(f"Создание чата: {chat_name}")

    def add_chat_view(self, avatar_url, name: str) -> None:
        chat_avatar = SelectableChatView(self.chatting_page.chats_list_scrollable_frame, avatar_url, name)
        chat_avatar.pack(side='top', anchor='ne', pady=5, padx=5, fill="x")

    def add_message_view(self, content_type: str, content: str) -> None:
        message = MessageView(self.chatting_page.chat_frame, content_type, content)
        message.pack(side='bottom', anchor='se', pady=5, padx=5, fill="x")

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
