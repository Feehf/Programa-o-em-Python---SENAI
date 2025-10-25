nota_1=float(input('Digite os pontos da 1° atividade:'))
nota_2=float(input('Digite os pontos da 2° atividade:'))
nota_3=float(input('Digite os pontos da 3° atividade:'))
total = (nota_1 + nota_2 + nota_3)/3


print(f'''
     Situação do aluno

      aprovado? - {total>=7}
      recuperação? - {total <=5 and total <7}
      reprovado? -  {total <=4}

      ''')

int(print('Sua nota é', total))