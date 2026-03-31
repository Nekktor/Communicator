import tkinter as tk
from start_page import StartPage
from chatting_page import ChattingPage
from adding_page import AddingPage
from sign_up_page import SignUpPage
from user import User


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")

        # Инициализация классов
        self.start_page = StartPage(self.root)
        self.chatting_page = ChattingPage(self.root, self.switch_to_adding_page)
        self.adding_page = AddingPage(self.root, self.switch_to_chatting_page, self.on_chat_adding_submit)
        self.sign_up_page = SignUpPage(self.root, self.register_user, self.login_user)
        self.user = None

    def remove_pages(self):
        self.start_page.hide_start_page()
        self.adding_page.hide_adding_page()
        self.chatting_page.hide_chatting_page()
        self.sign_up_page.hide_sign_up_page()

    def switch_to_chatting_page(self):
        self.remove_pages()
        self.chatting_page.show_chatting_page()

    def switch_to_sign_up_page(self):
        self.remove_pages()
        self.sign_up_page.show_sign_up_page()

    def switch_to_adding_page(self):
        self.remove_pages()
        self.adding_page.show_adding_page()

    def on_chat_adding_submit(self):
        # Здесь должна находится логика для добавления данных чата в БД
        pass

    def register_user(self):
        user_name = self.sign_up_page.name_entry.get()
        user_username = self.sign_up_page.username_entry.get()

        self.user = User(user_name, user_username)

        if self.user.registration_check(user_username):
            self.user.add_user(user_name, user_username)

            self.user.name = user_name
            self.user.username = user_username

            self.remove_pages()
            self.chatting_page.show_chatting_page()
        else:
            self.user = None

        # Временная мера
        self.remove_pages()
        self.chatting_page.show_chatting_page()

    def login_user(self):
        user_username = self.sign_up_page.username_entry.get()

        self.user = User('', user_username)

        if self.user.login_check(user_username):
            user_data = self.user.get_user_data(user_username)

            self.user.name = user_data['name']
            self.user.username = user_data['username']

            self.chatting_page.show_chatting_page()
        else:
            self.user = None

        # Временная мера
        self.chatting_page.show_chatting_page()

    def sign_up_error_callback(self, error: str):
        # Метод принимает название ошибки на вход и передаёт его на метод для её отображения
        self.sign_up_page.error_callback(error)

    def initialize(self):
        # Метод показывает стартовую страницу, затем главную
        self.start_page.show_start_page()
        self.root.after(2000, self.switch_to_sign_up_page)

    def run(self):
        # Метод запускающий программу
        self.initialize()
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

