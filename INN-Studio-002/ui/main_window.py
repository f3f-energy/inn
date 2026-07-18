import customtkinter as ctk
from git.git_manager import branch,status

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1200x700')
        self.title('INN Studio')
        ctk.CTkLabel(self,text='INN Studio 0.2',font=('Segoe UI',28,'bold')).pack(pady=20)
        ctk.CTkLabel(self,text='Branch: '+branch()).pack()
        ctk.CTkLabel(self,text='Git: '+status()).pack()
        ctk.CTkButton(self,text='Atualizar',command=self.refresh).pack(pady=20)
    def refresh(self):
        self.destroy()
        MainWindow().mainloop()
