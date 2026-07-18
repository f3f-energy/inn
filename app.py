import customtkinter as ctk
from pathlib import Path
import json
import os

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ROOT = Path(__file__).parent
VERSION_FILE = ROOT / "version.json"

# ==========================================================
# APP
# ==========================================================

class INNStudio(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("INN Studio")
        self.geometry("1400x900")
        self.minsize(1200, 700)

        self.load_version()

        self.create_sidebar()

        self.create_header()

        self.create_dashboard()

        self.create_statusbar()

    # ------------------------------------------------------

    def load_version(self):

        self.version = "0.1"

        if VERSION_FILE.exists():

            with open(VERSION_FILE, "r", encoding="utf8") as f:

                data = json.load(f)

                self.version = data.get("version", "0.1")

    # ------------------------------------------------------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(self, width=220)

        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(

            self.sidebar,

            text="INN Studio",

            font=("Segoe UI", 28, "bold")

        ).pack(pady=(25,5))

        ctk.CTkLabel(

            self.sidebar,

            text=f"v{self.version}"

        ).pack(pady=(0,25))

        menus = [

            "🏠 Dashboard",

            "🌿 Git",

            "📦 Backup",

            "📄 Documentação",

            "🗄 Banco",

            "☁ Deploy",

            "🦅 Águia",

            "⚙ Configurações"

        ]

        for m in menus:

            ctk.CTkButton(

                self.sidebar,

                text=m,

                height=40

            ).pack(fill="x", padx=15, pady=4)

    # ------------------------------------------------------

    def create_header(self):

        self.header = ctk.CTkFrame(self, height=55)

        self.header.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(

            self.header,

            text="INN 2.0 Foundation",

            font=("Segoe UI",22,"bold")

        ).pack(side="left", padx=20, pady=12)

    # ------------------------------------------------------

    def card(self,parent,titulo,valor):

        frame = ctk.CTkFrame(parent,width=250,height=120)

        frame.pack_propagate(False)

        frame.pack(side="left",padx=10,pady=10)

        ctk.CTkLabel(

            frame,

            text=titulo,

            font=("Segoe UI",16)

        ).pack(pady=(20,5))

        ctk.CTkLabel(

            frame,

            text=valor,

            font=("Segoe UI",24,"bold")

        ).pack()

    # ------------------------------------------------------

    def create_dashboard(self):

        self.main = ctk.CTkFrame(self)

        self.main.pack(fill="both",expand=True,padx=10)

        linha1 = ctk.CTkFrame(self.main)

        linha1.pack(fill="x")

        self.card(linha1,"Projeto","INN")

        self.card(linha1,"Versão","2.0")

        self.card(linha1,"Branch","desenvolvimento")

        self.card(linha1,"Git","OK")

        linha2 = ctk.CTkTextbox(self.main)

        linha2.pack(fill="both",expand=True,padx=10,pady=10)

        linha2.insert("0.0",

"""Bem-vindo ao INN Studio.

Este será o ambiente oficial de desenvolvimento da Inn Technology.

Próximos módulos:

• Git Manager

• Backup Manager

• Version Manager

• Deploy Manager

• Supabase Manager

• Águia

• IA

""")

        linha2.configure(state="disabled")

    # ------------------------------------------------------

    def create_statusbar(self):

        barra = ctk.CTkFrame(self,height=28)

        barra.pack(fill="x")

        ctk.CTkLabel(

            barra,

            text="Status: Pronto",

            anchor="w"

        ).pack(side="left",padx=10)

# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    app = INNStudio()

    app.mainloop()