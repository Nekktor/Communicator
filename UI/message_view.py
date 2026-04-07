import customtkinter as ctk

class MessageView(ctk.CTkFrame):
    def __init__(self, master, content_type: str, content: str):
        # fg_color — цвет фона (можно оставить по умолчанию или задать явно)
        # corner_radius — скругление углов
        super().__init__(master, corner_radius=10, border_width=1, border_color="gray")

        # Label для текста сообщения
        self.first_mes_label = ctk.CTkLabel(self, text=content)

        self.type = content_type
        self.content = content

        self.setup_initial_view()

    def setup_initial_view(self):
        self.first_mes_label.pack(side='top', padx=10, pady=5)