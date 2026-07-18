import customtkinter as ctk

class Toolbar(ctk.CTkFrame):
    def __init__(self,parent,on_backup=None,on_pull=None):
        super().__init__(parent)
        ctk.CTkButton(self,text='Backup',command=on_backup).pack(side='left',padx=5,pady=5)
        ctk.CTkButton(self,text='Git Pull',command=on_pull).pack(side='left',padx=5,pady=5)
