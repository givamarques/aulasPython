idade = int(input("digite sua idade: ")) #pode-se converter a string em int na mesma linha do input
peso = int(input("digite seu peso: "))
sono_noite_anterior = int(input("digite quantas horas dormiu noite passada: "))

if (idade >= 16) and (idade < 70) and (peso > 50) and (sono_noite_anterior > 5): #condicionais AND = precisa cumprir TODAS as condicionais
    print("voce pode doar sangue")
else:
    print("voce NAO pode doar sangue")