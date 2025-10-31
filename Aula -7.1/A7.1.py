variavel = 10
lista =  []
tuplas = ()

numeros_pares  = list(range(2,21,2))
print(numeros_pares)

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

i = numeros.index(3)
print(numeros[i])

numeros.append(9)

print(numeros)


i = numeros.index(5)
numeros.pop(i)


carros = ['Ferrari','Jeep','Mercedes']

print(numeros,carros)

numeros += (carros)

print(numeros)

pessoa = ("Maria", 28, "123.456.789-00")

nome, idade, cpf = pessoa
print(nome)   # Maria
print(idade)  # 28
print(cpf)    # 123.456.789-00

print(pessoa)

pessoas = [
    {"nome": "Maria", "idade": 28, "cpf": "123.456.789-00"},
    {"nome": "João", "idade": 35, "cpf": "987.654.321-00"},
    {"nome": "Ana", "idade": 22, "cpf": "111.222.333-44"}
]

for pessoa in pessoas:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    cpf = "".join(pessoa["cpf"])
    print(f"{nome}, {idade} anos, CPF: {cpf}")
