lista = [1, 2, 3]
print ("Tamanho de lista:", len(lista))

lista[0]=9
print("-----------")
for i in range(len(lista)):
    print (lista[i])


## Remover e adicionar na lista

convidados = [] #define uma lista vazia
convidados.append ('Exemplo 1')
convidados.append (' Exemplo 2')
convidados.append (' Exemplo 3')
convidados.append (' Exemplo 4')
print ("Tenho ", len(convidados)," Convidados")
convidados.sort() # colocando em ordens
print ("Sao eles:")
print (convidados)
print ("O primeiro convidado eh o ",convidados[0])
convidados.remove("Exemplo 4"); #aqui tiramos o Exemplo 4 da lista
print ("Agora tenho somente ", len(convidados)," Convidados")
print ("Sao eles:")
for convidado in convidados:
    print (convidado)
