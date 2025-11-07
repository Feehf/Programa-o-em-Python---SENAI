# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.


# try:
#     n = int(input('Insira um número:'))
#     print(n)
# except:
#     print('O dado informado é incorreto:')

# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# def divisão():
#     try:
#         n1 = float(input('Digite o seu número:'))
#         n2 = float(input('Digite um novo número:  '))
#         div = (n1/n2)
#         print(div)

#     except ZeroDivisionError:
#         print('Zero não pode ser dividido')
#     except ValueError:
#         print('Um texto foi digitado')
#     except TypeError as erro:
#         print(erro)

#     else:
#         print('Execução foi um sucesso')

# divisão()

# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

# def lista():
#     lista = [0,1,2,3,4,5,6,7,8,9,10]
#     try:
#         indice = int(input('Digite o número que deseja ver da lista:'))
#         print(lista[indice])

#     except ValueError:
#         print('Foi digitado um valor inválido')
#     except IndexError:
#         print('Esse indice não existe')
# lista()

def imc(peso, altura):
    peso = float(input('Peso:  '))
    altura = float(input('Altura: '))
    return peso/altura**2
    print(imc(peso, altura)**2)
