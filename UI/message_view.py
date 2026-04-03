import tkinter as tk

class MessageView(tk.Frame):
    def __init__(self, master, content_type: str, content):
        tk.Frame.__init__(self, master, bd=1, relief='solid')

        first_mes_label = tk.Label(self, text=content)
        first_mes_label.pack(side='top')

        self.type = content_type
        self.content = content