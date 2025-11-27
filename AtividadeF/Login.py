import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from PIL import Image, ImageTk
import customtkinter

def abrir_sistema():
    login.destroy()

    subprocess.Popen([sys.executable, 'Atividade.py'])

login =  customtkinter.CTk()
login.configure(fg_color='royalblue3')

login = tk.Tk()
login.title("Sistema Hospitalar - Login")
login.geometry("700x630")
login.resizable(False, False)


frame = ttk.Frame(login, padding=20)
frame.pack(expand=True)

titulo = ttk.Label(frame, text="Cadastro de Paciente", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

botao = ttk.Button(frame, text="Entrar no Sistema", command=abrir_sistema)
botao.pack(pady=20)

login.mainloop()
