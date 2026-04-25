import customtkinter as ctk


class ErrorHandler(ctk.CTkToplevel):
    def __init__(self, master, error_text: str):
        super().__init__(master)

        self.title('Error')
        self.error_text = error_text

        # 1. Исправлено создание текстового поля
        self.error_label = ctk.CTkTextbox(
            self,
            text_color='red',
            font=('Arial', 14),
            width=300,  # Желательно задать размеры
            height=150
        )
        self.error_label.insert("0.0", self.error_text)

        # 2. Сначала размещаем элементы
        self.setup_initial_view()

        # 3. Затем центрируем (после того как размеры заданы)
        self.center_window(self, master)

        self.after(10, lambda: self.focus_force())

    @staticmethod
    def center_window(window, master):
        window.update_idletasks()

        p_w, p_h = master.winfo_width(), master.winfo_height()
        p_x, p_y = master.winfo_rootx(), master.winfo_rooty()
        t_w, t_h = window.winfo_width(), window.winfo_height()

        x = p_x + (p_w // 2) - (t_w // 2)
        y = p_y + (p_h // 2) - (t_h // 2)
        window.geometry(f"+{x}+{y}")

    def setup_initial_view(self):
        self.error_label.pack(expand=True, fill="both", padx=10, pady=10)
        self.resizable(False, False)
        self.focus_force()
