#o aluno só é aprovado se conseguir nota 7

nota1 = input("insira a primeira nota: ")
nota1 = int(nota1)
nota2 = input("insira a segunda nota: ")
nota2 = int(nota2)

media = (nota1 + nota2) / 2

if (media >= 7):
    print("parabens! voce foi aprovado!") #identacao = 4 espacos
else:
    print("você está na recuperação.")