import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

def conect():
    return sqlite3.connect('Dados_Pacientes.db')

def criar_tabela():
    conn =  conect()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
              ID INTEGER PRIMARY KEY,
              Nome  TEXT,
              CPF TEXT,
              Idade INTEGER,
              IMC INTEGER

              )   
              ''')
    
    conn.commit()
    conn.close() 
   
# create
def inserir_usuario():
    cpf  = CPF_entry.get().strip()
    nome = nome_entry.get().strip()
    idade = idade_entry.get().strip()
    peso = peso_entry.get().strip()
    altura = altura_entry.get().strip()

#Calculo de IMC
    peso = peso_entry
    altura = altura_entry.get()
    imc = peso/(altura * altura)


    if not (cpf and nome and idade):
        messagebox.showwarning('', 'INSIRA OS DADOS SOLICITADOS')
        return

    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showwarning('', 'O CPF informado é inválido')
        return

    conn = conect()
    c = conn.cursor()
    c.execute('INSERT INTO usuarios (nome, cpf, idade) VALUES (?,?,?)', (nome, cpf, idade))
    conn.commit()
    conn.close()


    messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')
    mostrar_usuario()


# read 
def mostrar_usuario(): 
    for row in tree.get_children():
        tree.delete(row)
        
    conn =  conect()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuario = c.fetchall()
    for us in usuario:
        tree.insert("", "end",values = (us[0],us[1],us[2],us[3],us[4]))
    conn.close()    



# atualizar
def atualizar():
    selecao = tree.selection()
    if selecao:
        
        dado_edit = tree.item(selecao)['values'][0]
        novo_cpf = CPF_entry.get()
        novo_nome = nome_entry.get()
        novo_idade = idade_entry.get()


        if novo_cpf and novo_nome and novo_idade:
            conn =  conect()
            c = conn.cursor()

            c.execute("UPDATE usuarios SET  nome = ?, cpf =?, idade = ? WHERE nome = ? ", (novo_nome, novo_cpf, novo_idade, dado_edit))
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
        conn =  conect()
        c = conn.cursor()     
        c.execute("DELETE FROM usuarios WHERE nome = ?", (user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('', 'ERRO AO DELETAR O DADO')    

# interface grafica
# grid  

janela =  customtkinter.CTk()
janela.configure(fg_color='royalblue3')
janela.title('SI4 -  Cadastro ')
janela.geometry('1000x730')
caminho = 'HC.ico'
janela.iconbitmap(caminho)


tk.Label(janela, text = 'Cadastro de paciente', font=('arial', 15)).grid(row=0, column=0, pady=10, padx=10)


fr0 =  customtkinter.CTkFrame(janela )
fr0.grid(columnspan=3)



nome_label =  tk.Label(fr0, text='Nome', font=('arial', 15))
nome_label.grid(row=1, column=0, pady=10, padx=10)

nome_entry = tk.Entry(fr0, font=('arial', 15))
nome_entry.grid(row=1, column=1, pady=10, padx=10)

CPF_label =  tk.Label(fr0, text='CPF', font=('arial', 15))
CPF_label.grid(row=2, column=0, pady=10, padx=10)

CPF_entry = tk.Entry(fr0, font=('arial', 15))
CPF_entry.grid(row=2, column=1, pady=10, padx=10)

idade_label =  tk.Label(fr0, text='Idade', font=('arial', 15))
idade_label.grid(row=4, column=0, pady=10, padx=10)

idade_entry = tk.Entry(fr0, font=('arial', 15))
idade_entry.grid(row=4, column=1, pady=10, padx=10)

altura_label =  tk.Label(fr0, text='altura', font=('arial', 15))
altura_label.grid(row=5, column=0, pady=10, padx=10)

altura_entry = tk.Entry(fr0, font=('arial', 15))
altura_entry.grid(row=5, column=1, pady=10, padx=10)

peso_label =  tk.Label(fr0, text='peso', font=('arial', 15))
peso_label.grid(row=6, column=0, pady=10, padx=10)

peso_entry = tk.Entry(fr0, font=('arial', 15))
peso_entry.grid(row=6, column=1, pady=10, padx=10)

fr =  customtkinter.CTkFrame(janela)
fr.grid( columnspan=2)


btn_salvar =  customtkinter.CTkButton(fr, text= 'SALVAR', font=('arial', 15), command=inserir_usuario, fg_color='dodgerblue2')
btn_salvar.grid(row=7, column=0, padx=10, pady=10)

btn_atualizar =  customtkinter.CTkButton(fr, text= 'ATUALIZAR', font=('arial', 15), command=atualizar,fg_color='dodgerblue2')
btn_atualizar.grid(row=7, column=2, padx=10, pady=10)

btn_delete =  customtkinter.CTkButton(fr, text= 'DELETAR', font=('arial', 15), command=delete_usuario, fg_color='dodgerblue2')
btn_delete.grid(row=7, column=3, padx=10, pady=10)

fr2 = customtkinter.CTkFrame(janela)
fr2.grid( columnspan=2)

colunas = ('ID', 'NOME', 'CPF', 'IDADE', 'IMC')
tree =  ttk.Treeview(fr2, columns=colunas, show='headings', height=40)
tree.grid(row=6, column=0,padx=5, sticky='nsew')


for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)

criar_tabela()
mostrar_usuario()


janela.mainloop()




     