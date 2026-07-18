import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("INN Studio")
        self.geometry("1400x900")
        ctk.CTkLabel(self,text="INN Studio v0.1",font=("Segoe UI",28,"bold")).pack(pady=40)
