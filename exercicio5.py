primeiro_numero = int(input("digite o primeiro numero: ")) #ao inves de numero1 use primeiro_numero
segundo_numero = int(input("digite o primeiro numero: "))

soma = primeiro_numero+segundo_numero

if (soma > 20 ):
    soma = soma + 8
    print(soma)
else:
    soma = soma - 5
    print(soma)