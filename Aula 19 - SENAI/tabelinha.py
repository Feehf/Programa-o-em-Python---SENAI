import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

def conectar():
    return sqlite3.connect('Banquinho.db')

def criar_tabela():
    conn =  conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
              cpf  TEXT,
              nome TEXT,
              email TEXT

              )   
              ''')
    conn.commit()
    conn.close() 
   
# create
def inserir_usuario():
    cpf  =  CPF_entry.get()
    nome = nome_entry.get()
    email = email_entry.get()

    if cpf and nome and email:
        conn =  conectar()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios VALUES(?,?,?)", (cpf, nome, email))
        conn.commit()
        conn.close()   
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')  
        mostrar_usuario()
    else:
        messagebox.showwarning('','INSIRA OS DADOS SOLICITADOS')

# read 
def mostrar_usuario(): 
    for row in tree.get_children():
        tree.delete(row)
        
    conn =  conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuario = c.fetchall()
    for us in usuario:
        tree.insert("", "end",values = (us[0], us[1],us[2]))
    conn.close()    



# atualizar
def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit = tree.item(selecao)['values'][0]
        novo_cpf = CPF_entry.get()
        novo_nome = nome_entry.get()
        novo_email = email_entry.get()

        if novo_cpf and novo_nome and  novo_email:
            conn =  conectar()
            c = conn.cursor()
            c.execute("UPDATE usuarios SET  nome = ?, email = ? , cpf =?  WHERE cpf = ? ", (novo_nome, novo_email, novo_cpf , dado_edit))
            conn.commit()
            conn.close()   
            messagebox.showinfo('', 'DADOS ATUALIZADOS COM SUCESSO!')  
            mostrar_usuario()
        else:
            messagebox.showwarning('','TODOS OS DADOS PRECISAM SER PREENCHIDOS ')
            
   
    
# delete 
def delete_usuario():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][0]
        conn =  conectar()
        c = conn.cursor()     
        c.execute("DELETE FROM usuarios WHERE cpf = ?", (user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('', 'ERRO AO DELETAR O DADO')    

    

# interface grafica
# grid  

janela =  customtkinter.CTk()
janela.configure(fg_color='gray')
janela.title('CRUD  -  FORM ')
janela.geometry('700x630')
caminho = 'icone.ico'
janela.iconbitmap(caminho)


tk.Label(janela, text = 'FORMULÁRIO ', font=('arial', 15)).grid(row=0, column=0, pady=10, padx=10)


fr0 =  customtkinter.CTkFrame(janela )
fr0.grid(columnspan=3)

CPF_label =  tk.Label(fr0, text='CPF', font=('arial', 15))
CPF_label.grid(row=1, column=0, pady=10, padx=10)

CPF_entry = tk.Entry(fr0, font=('arial', 15))
CPF_entry.grid(row=1, column=1, pady=10, padx=10)

nome_label =  tk.Label(fr0, text='Nome', font=('arial', 15))
nome_label.grid(row=2, column=0, pady=10, padx=10)

nome_entry = tk.Entry(fr0, font=('arial', 15))
nome_entry.grid(row=2, column=1, pady=10, padx=10)


email_label =  tk.Label(fr0, text='E - mail', font=('arial', 15))
email_label.grid(row=3, column=0, pady=10, padx=10)

email_entry = tk.Entry(fr0, font=('arial', 15))
email_entry.grid(row=3, column=1, pady=10, padx=10)


fr =  customtkinter.CTkFrame(janela)
fr.grid( columnspan=2)


btn_salvar =  customtkinter.CTkButton(fr, text= 'SALVAR', font=('arial', 15), command=inserir_usuario, fg_color='purple')
btn_salvar.grid(row=5, column=0, padx=10, pady=10)

btn_atualizar =  customtkinter.CTkButton(fr, text= 'ATUALIZAR', font=('arial', 15), command=atualizar,fg_color='purple')
btn_atualizar.grid(row=5, column=2, padx=10, pady=10)

btn_delete =  customtkinter.CTkButton(fr, text= 'DELETAR', font=('arial', 15), command=delete_usuario, fg_color='purple')
btn_delete.grid(row=5, column=3, padx=10, pady=10)

fr2 = customtkinter.CTkFrame(janela)
fr2.grid( columnspan=2)

colunas = ('CPF', 'NOME', 'E-MAIL')
tree =  ttk.Treeview(fr2, columns=colunas, show='headings', height=40)
tree.grid(row=6, column=0,padx=5, sticky='nsew')


for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)

criar_tabela()
mostrar_usuario()


janela.mainloop()




     
