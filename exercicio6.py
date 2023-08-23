numero_a_ser_adivinhado = 20

while True:
    palpite = int(input("Digite seu palpite: "))
    if numero_a_ser_adivinhado == palpite:
        print("Parabens, voce acertou!")
        break
    if palpite > numero_a_ser_adivinhado:
        print("Tente um numero MENOR")
    else:
        print("Tente um numero MAIOR")
