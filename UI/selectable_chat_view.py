import customtkinter as ctk
from PIL import Image, ImageTk

class SelectableChatView(ctk.CTkFrame):
    def __init__(self, master, avatar_url, name):
        super().__init__(master, height=60, border_width=1)

        self.pack_propagate(False)

        self.master = master
        self.avatar_url = avatar_url


        # Отображение иконки чата
        if self.avatar_url is not None:
            self.image = Image.open(self.avatar_url)
            self.avatar_image = ctk.CTkImage(dark_image=self.image, size=(40, 40))
        else:
            self.image = Image.open('./assets/no_image.jpg')
            self.avatar_image = ctk.CTkImage(dark_image=self.image, size=(40, 40))

        self.avatar = ctk.CTkLabel(self, image=self.avatar_image, text="")

        # Отображение имени чата
        self.name = ctk.CTkLabel(self, text=name, text_color="white", font=("Arial", 14))

        self.setup_initial_view()

    def setup_initial_view(self):
        self.avatar.pack(side="left", pady=5, padx=5)
        self.name.pack(side="left", padx=5, anchor="center")
