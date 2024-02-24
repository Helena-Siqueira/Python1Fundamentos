# Como percorrer uma lista com laço FOR
# Percorrer a lista é o mesmo que passar pot todos os itens da lista, um por um, e fazer alumaa ação cada um deles, como por exemplo, mostrar

lista_frutas = ["Maça", "", "Banana", "Pera", "", "Uva", "Abacaxi", "", "Tomate"]

frutas_encontradas = 0

for contador in range (len(lista_frutas)):

    if lista_frutas[contador] != "":
        frutas_encontradas +=1
        print(f"{frutas_encontradas} - {lista_frutas [contador].upper()}")
        


