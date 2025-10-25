#  A função print funciona para imprimir algo  print('Imprime um texto para o usuário') se for print (Imprime uma váriavel)
#   + soma - subtração * divisão

# SISTEMA DE MÉDIA DE ALUNO

# 1 -  Criar 3 variáveis, notas, tipo float()***

# 2 -   Mostre no console a média das 3 variáveis***

# 3 - Passou de ano?  -  media >= 7***

nota=float(input('Digite os pontos da 1° atividade:'))
nota1=float(input('Digite os pontos da 2° atividade:'))
nota2=float(input('Digite os pontos da 3° atividade:'))

total = (nota + nota1 + nota2)/3

if total >= 7:
 round(print('Parabens você passou! sua nota', total))

elif total <= 5:
  round(print("Você está de recuperação, sua nota", total))

else:
  round(print('Você reprovou! Sua nota é', total))
