import tkinter as tk

class StartPage:
    def __init__(self, master):
        """
        Создание, отображение и скрытие начальной страницы, появляющейся перед входом в приложение

        :param master: Главное окно приложения, находится в main
        """

        # Рамка в которой размещаются элементы данного окна
        self.frame = tk.Frame(master, height=600, width=800)

        # Элементы стартовой страницы
        self.welcome_label = tk.Label(self.frame, text="Welcome to Communicator!", font=("Arial", 25))

        # Размещение элементов на экране
        self.welcome_label.pack(pady=100)

    def show_start_page(self):
        self.frame.pack(fill="both", expand=True)

    def hide_start_page(self):
        self.frame.pack_forget()




