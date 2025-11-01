# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

print('Verifique se o seu número é positivo ou negativo>>>>>>'
       )

 numero = int(input('Digite o seu número:'))

if numero <0:
     print('Seu número é negativo')
elif numero >0:
     print('Seu número é positivo')
else:
     print('Nulo')

 # 2*
 # Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
 # base na idade.

print('Bem vindo a votação! Vamos verificar se você pode votar>>')

idade = int(input('Digite sua idade'))

if idade >16:
  print('Você pode votar!')

else:
    print('Seja bem vindo(a) a votação!')

# 3*

# # Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

aleatorio = 2

if aleatorio %2==0:

 print('Seu número é par')
else:
 print('Seu número é impar')

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

triangulo = int(input('Digite aqui:' ))
lado_2 = int(input('Digite aqui:'))
lado_3 = int(input('Digite aqui:'))

if triangulo == lado_2 == lado_3:
   print