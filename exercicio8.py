lista_frutas=["maca", "laranja", "uva", "pera", "banana"]
print(lista_frutas)

print(lista_frutas[0:1]) #neste caso printa do indice zero ate 1, sendo que o 1 não é impresso
#cod acima só vai mostrar 'maca', tem que colocar o ultimo indice sempre 1 acima do desejado

print(len(lista_frutas))
#len eh um metodo usado para saber o tamanho da lista, como em length

lista_frutas.append("caju")
print(lista_frutas)
#lista é um objeto, para adicionar pode usar metodo APEND e retirar pode usar metodo REMOVE

print(len(lista_frutas))
#len eh um metodo usado para saber o tamanho da lista, como em length

lista_frutas.remove("laranja")
print(lista_frutas)

print(len(lista_frutas))
#len eh um metodo usado para saber o tamanho da lista, como em length

print(sorted(lista_frutas))
#sorted lista em ordem crescente

lista_frutas.reverse() #reverse lista em ordem decrescente
print(lista_frutas)
