# Lista em Python (arrays e vetores)
 
# Para criar listas criamos COLCHETES[]
# Os itens dentro da lista são separados por vírgula
lista_nomes = [ "Conradito", "Pedrita", "Marina", "Lucas"]

# Exibir toda lista
print( lista_nomes )

# Exibir um item especifico da lista 
print( lista_nomes [0] )
print( lista_nomes [3])

# Como trocar um item da lista
print(f"Antes era {lista_nomes[2]}")
lista_nomes [2] = "Mônica"
print(f"E agora é {lista_nomes[2]}")

# Adicionar um item novo na lista
lista_nomes.append("Douglas")
lista_nomes.append("Maira")

print(lista_nomes)

# Contar quantos itens existe na lista  
print(f"A lista tem {len (lista_nomes)} nomes")

# Romover um item da lista - PELO NOME 
lista_nomes.remove("Douglas")
print(lista_nomes)

# Romover um item da lista - PELO ÍNDICE
lista_nomes.remove( lista_nomes[1]) 
#lista_nomes[1] = ""
print(lista_nomes)