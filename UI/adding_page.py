import tkinter as tk

class AddingPage(tk.Frame):
    def __init__(self, master, back_to_chats, on_chat_adding_submit):
        """
        UI обрабатывающий создание нового чата (Надписи могут быть изменены в соответствии с вводимыми данными)

        :param master: Главное окно Tkinter, находится в main
        :param back_to_chats: Метод, перемещающий пользователя на страницу с чатами, находится в main
        :param on_chat_adding_submit: Метод, отвечающий за обработку данных, введённых пользователем, находится в main
        """
        super().__init__(master)
        self.master = master
        self.returning = back_to_chats
        self.submitting = on_chat_adding_submit

        # Рамка на которой размещены элементы окна
        self.adding_page = tk.Frame(self.master, relief="solid", bd=5)

        # Поля для ввода информации для создания
        self.chat_name_entry = tk.Entry(self.adding_page)
        self.participants_entry = tk.Entry(self.adding_page)

        self.chat_name_label = tk.Label(self.adding_page, text='Введите название для чата')
        self.participants_label = tk.Label(self.adding_page, text='Перечислите добавляемых пользователей')

        # Кнопки перемещения
        self.back_button = tk.Button(self.adding_page, text="Вернуться к чатам", width=25, height=3, command=self.returning)
        self.submit_button = tk.Button(self.adding_page, text="Подтвердить", width=25, height=3, command=self.submitting)

        # Размещение элементов на экране
        self.chat_name_label.pack(side="top", pady=10)
        self.chat_name_entry.pack(side="top", pady=10)

        self.participants_label.pack(side="top", pady=10)
        self.participants_entry.pack(side="top", pady=10)

        self.back_button.place(x=100, y=500)
        self.submit_button.place(x=500, y=500)

    def show_adding_page(self):
        self.adding_page.pack(expand=True, fill="both")

    def hide_adding_page(self):
        self.adding_page.pack_forget()