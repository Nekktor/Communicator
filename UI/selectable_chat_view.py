import customtkinter as ctk
from PIL import Image

class SelectableChatView(ctk.CTkFrame):
    def __init__(self, master, avatar_url: str, name: str, last_message: str, **kwargs):
        super().__init__(master, height=60, border_width=1, **kwargs)

        self.pack_propagate(False)

        self.master = master
        self.avatar_url = avatar_url
        self.name = name
        self.last_message = last_message

        # Отображение иконки чата
        if self.avatar_url != '':
            self.image = Image.open(self.avatar_url)
            self.avatar_image = ctk.CTkImage(dark_image=self.image, size=(50, 50))
        else:
            self.image = Image.open('./assets/no_image.jpg')
            self.avatar_image = ctk.CTkImage(dark_image=self.image, size=(50, 50))

        self.avatar = ctk.CTkLabel(self, image=self.avatar_image, text="")
        self.avatar.grid_propagate(False)

        # Отображение имени чата
        self.name_label = ctk.CTkLabel(self, text=self.name, text_color="white", font=("Arial", 14))

        # Отображение последнего сообщения в чате
        self.last_message_label = ctk.CTkLabel(self, text=self.last_message, text_color="gray", font=("Arial", 12))

        self.setup_initial_view()

    def setup_initial_view(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.avatar.grid(column=0, row=0, rowspan=2, pady=5, padx=5, sticky="nsew")
        self.name_label.grid(column=1, row=0, sticky="sw", pady=5)
        self.last_message_label.grid(column=1, row=1, sticky="nw", pady=5)
