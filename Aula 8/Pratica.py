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

lado1 = int(input('Digite aqui:' ))
lado2 = int(input('Digite aqui:'))
lado3 = int(input('Digite aqui:'))

if lado1 == lado2 == lado3:
   print('Seu triângulo é Equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
   print('Seu triângulo é isósceles')

else:
   print('Seu triângulo é escaleno')

# 5*

# Determine se um número é múltiplo de 5 e 7.

numero = int(input('Digite seu número para calcular se ele é multiplo de 5 ou 7.'))

if numero %5 == 0:
 print('Seu número é divizivel por 5')

elif numero %7 == 0:
   print('Seu número é divizivel por 7')

else:
   print('Não é divizivel')

   # 6*

# Verifique se um número é positivo e maior que 10

numero = int(input('digite seu número para verificarmos se ele é maior que 10 ou se ele é positivo'))

if numero >10:
   print('Seu nú,ero é maior que 10')

elif numero >=0:
   print('Seu número é positivo')
   
else:
   print('Seu número é negativo')

   # 7*

# Verifique se um número é divisível por 3 ou 5.

numero = int(input('Digite seu número para verificarmos se ele é divisivel por 3 ou 5'))

if numero %3 == 0:
   print('Seu número é divisivel por 3')
elif numero %5 == 0:
   print('Seu número é divisivel por 5')

else:
   print('Seu número não é divisivel por 5 ou 7')
    
