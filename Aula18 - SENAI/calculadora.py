import tkinter as tk


def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ +  n2_
    resultado.config(text=soma) 

def sub():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    sub  = n1_ -  n2_
    resultado.config(text=sub) 


def multi():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    multi  = n1_ *  n2_
    resultado.config(text=multi) 


def div():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    div  = n1_ /  n2_
    resultado.config(text=dvs) 


root = tk.Tk()
root.geometry('250x370')


n1_label =  tk.Label(root, text='N1', font=('arial',12))
n1_label.grid(pady=5, column=1, row =1 )

n1 =  tk.Entry(root, font=('arial',12))
n1.grid(row=1, column=2, padx=5)

n2_label =  tk.Label(root, text='N2', font=('arial',12))
n2_label.grid(pady=5, column=1, row =3 )

n2 =  tk.Entry(root, font=('arial',12))
n2.grid(row=3, column=2, padx=5)

btn_soma =  tk.Button(root, text= '+', font=('arial',10), command=mostrar_resultado_soma)
btn_soma.grid(row=4, column= 1, pady=5)

bnt_sub = tk.Button(root, text= '-', font=('arial', 12), command=sub)
bnt_sub.grid(row=5, column= 1, pady=5)

bnt_multi= tk.Button(root, text= 'x', font=('arial', 12), command=multi)
bnt_multi.grid(row=6, column= 1, pady=5)


bnt_div= tk.Button(root, text= '/', font=('arial', 12), command= div)
bnt_div.grid(row=7, column= 1, pady=5)



# crie mais 3  botões e evoque as funções 


resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 6, column=2)



root.mainloop()

