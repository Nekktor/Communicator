import customtkinter as ctk

class MessageView(ctk.CTkFrame):
    def __init__(self, master, content_type: str, content: str, sender: str):
        super().__init__(master, corner_radius=15, border_width=1, border_color="gray")

        self.type = content_type
        self.content = content
        self.sender = sender

        if self.sender == 'User':
            self.sender_view = 'Вы'
        else:
            self.sender_view = self.sender

        # Label для имени отправителя
        self.sender_label = ctk.CTkLabel(self, text=self.sender_view, font=("Arial", 12), text_color="#20B2AA")

        # Label для текста сообщения
        self.message_label = ctk.CTkLabel(self, text=self.content, font=("Arial", 14))

        self.setup_initial_view()

    def setup_initial_view(self):
        self.sender_label.pack(side='top', anchor='ne', pady=(5, 0), padx=10)
        self.message_label.pack(side='top', anchor='sw', pady=(0, 5), padx=10)