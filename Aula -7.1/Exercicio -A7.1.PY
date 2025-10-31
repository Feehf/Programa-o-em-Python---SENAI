# e_commerce = {
# 'livros':{


# 'A':50.0,
# 'B':70.0,  


# },
# 'tablets':{
#     'a':15000.55,
#     'b':456.5,
# },
# 'fones':{
#    'a':500.0,
#    'b':750.0, 
# }


# }



 
# minhas_compras = {
# 'carrinho' : [],
# 'valores':[]
# }



# secao = input('livros, tablets ou fones ')
# prod1 = input('A ou B  ')


# minhas_compras['carrinho'].append(prod1)
# minhas_compras['valores'].append(e_commerce[secao][prod1])
# print(minhas_compras)

e_commerce = {
'livros':{


'ARARI':50.0,
'TALEB':70.0,  


},
'tablets':{
    'SAMSUMG':15000.55,
    'NOKIA':456.5,
},
'fones':{
   'JBL':500.0,
   'APPLE':750.0, 
}


}



 
minhas_compras = {
'carrinho' : [],
'valores':[]
}



secao1 = input('livros, tablets ou fones ')
prod1 = input(f'{e_commerce[secao1]}')


secao2 = input('livros, tablets ou fones ')
prod2 = input(f'{e_commerce[secao2]}')


secao3 = input('livros, tablets ou fones ')
prod3 = input(f'{e_commerce[secao3]}')


minhas_compras['carrinho'].append(prod1)
minhas_compras['valores'].append(e_commerce[secao1][prod1])
print(minhas_compras)


minhas_compras['carrinho'].append(prod2)
minhas_compras['valores'].append(e_commerce[secao2][prod2])
print(minhas_compras)


minhas_compras['carrinho'].append(prod3)
minhas_compras['valores'].append(e_commerce[secao3][prod3])
print(minhas_compras)



soma =  sum(minhas_compras['valores'])
