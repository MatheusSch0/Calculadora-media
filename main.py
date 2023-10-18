nota1 = float(input('Digite a nota aluno 1: '))
nota2 = float(input('Digite a nota aluno 2: '))
nota3 = float(input('Digite a nota aluno 3: '))

media = (nota1 + nota2 + nota3) / 3
#print(media)
if media >= 7:
  print("resultado = Aprovado")
elif media >= 5:
  print('resultado = Recuperação')
else:
  print('resultado = Reprovado')

print('Sua media será:',media)

