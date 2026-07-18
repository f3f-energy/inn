import customtkinter as ctk
from ui.toolbar import Toolbar
from backup.backup_manager import create_backup
from core.settings import PROJECT_PATH

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("INN Studio")
        self.geometry("1200x700")
        self.status=ctk.CTkLabel(self,text="Pronto")
        self.status.pack(side="bottom",fill="x")
        Toolbar(self,on_backup=self.do_backup,on_pull=self.do_pull).pack(fill="x")
        ctk.CTkLabel(self,text="INN Studio 0.5",font=("Segoe UI",28,"bold")).pack(pady=30)
    def do_backup(self):
        try:
            arq=create_backup(PROJECT_PATH)
            self.status.configure(text=f"Backup: {arq}")
        except Exception as e:
            self.status.configure(text=str(e))
    def do_pull(self):
        self.status.configure(text="Git Pull (integração completa na próxima versão)")
