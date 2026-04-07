import customtkinter as ctk


class ChattingPage(ctk.CTkFrame):
    def __init__(self, master, switch_to_adding_page, **kwargs):
        # Инициализируем базовый класс CTkFrame
        super().__init__(master, corner_radius=0, **kwargs)

        self.switch_to_adding_chat = switch_to_adding_page

######### --- Левая панель: список чатов --- #########

        self.chats_list_frame = ctk.CTkFrame(
            self,
            width=300,
            corner_radius=0,
            border_width=1,
            border_color="gray"
        )
        self.chats_list_frame.pack_propagate(False)

        # Область для списка чатов
        self.chats_list_scrollable_frame = ctk.CTkScrollableFrame(
            self.chats_list_frame,
            border_width=1
        )

        self.add_new_chat_button = ctk.CTkButton(
            self.chats_list_frame,
            height=38,
            text='Добавить новый чат',
            command=self.switch_to_adding_chat
        )

######### --- Правая панель: окно чата --- #########

        self.chat_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            border_width=1,
            border_color="gray"
        )
        # Убираем pack_propagate(False), чтобы фрейм подстраивался под контент,
        # либо оставляем его, если планируем жестко фиксировать размеры.

        self.setup_initial_view()

    def setup_initial_view(self):
        self.chats_list_frame.pack(side="left", fill="y")
        self.chats_list_scrollable_frame.pack(side="top", pady=10, padx=5, fill="both", expand=True)
        self.add_new_chat_button.pack(side="bottom", pady=5, padx=5, fill="x")
        self.chat_frame.pack(side="right", fill="both", expand=True)

    def show_chatting_page(self):
        self.pack(fill="both", expand=True)

    def hide_chatting_page(self):
        self.pack_forget()
