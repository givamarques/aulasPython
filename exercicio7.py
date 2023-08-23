total = 0
imposto = 0.1

while True:
    valor_item = input("Digite o valor do item ou 's' para sair: ")
    if valor_item=='s': #aqui é determinado como sair do programa
        break #o break dentro do escopo do if parando o programa
    total = total+float(valor_item) #valor total sendo atualizado com os valores somados do tipo float
    
total = total*imposto +total #valor total sendo atualizado incidindo o imposto

print("o valor total é: ", total) #imprime valor total atualizado já somado e com imposto