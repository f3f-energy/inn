import customtkinter as ctk
class StatusBar(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,height=28)
        self.label=ctk.CTkLabel(self,text='Pronto',anchor='w')
        self.label.pack(side='left',padx=8)
    def set(self,text):
        self.label.configure(text=text)
