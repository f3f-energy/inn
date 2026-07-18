import customtkinter as ctk
from explorer.project_tree import list_files

class ProjectPanel(ctk.CTkFrame):
    def __init__(self,parent,project):
        super().__init__(parent)
        self.box=ctk.CTkTextbox(self)
        self.box.pack(fill='both',expand=True)
        for item in list_files(project):
            self.box.insert('end',item+'\n')
        self.box.configure(state='disabled')
