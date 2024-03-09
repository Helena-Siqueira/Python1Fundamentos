# Sistema de vendas para lojas

import datetime
import os

def esta_na_lista(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False    

vendedor_esta_logado = False
vendas = []

vendedores = [123, 456]

produtos = [
    "Notebook Dell",
    "Smartphone Samsung",
    "Smart TV LG",
    "Forno Elétrico",
    "Câmera Canon"
]

print("Olá, bem-vindo ao sistema de produtos da loja!")

while True:

    while not vendedor_esta_logado:
        print("Entre com seu código de vendedor:")
        codigo_vendedor = int(input())
        #for i in range(len(vendedores)):
            #if vendedores[i] == codigo_vendedor:
        vendedor_esta_logado = esta_na_lista(codigo_vendedor, vendedores)
    
    print("\n\nOpções disponíveis com produtos:")
    print("1 - Cadastar")
    print("2 - Vendas")
    print("3 - Exibir todos produtos")
    print("4 - Pesquisar por um produto")
    print("5 - Sair")
    print("Digite a opção desejada:")
    resposta = input()
    os.system("cls")

    # CADASTRAR UM PRODUTO
    if resposta == "1": 
        print("Digite o nome do produto para cadastrar:")
        nome = input()
        # - Verificar se o nome é menor que 3 caracteres
        produtos.append( nome ) # Adiciona produto na lista
        print("Produto cadastrado com sucesso!")

    # SISTEMA DE VENDAS
    if resposta == "2":
        print("Digite 1 para VENDER ou 2 para LISTAR")
        resposta = input()

        # VENDER
        if resposta == "1":
            print("Digite o ID do produto:")
            id = int( input() )
            # - Verificar se existe o índice na lista
            item = produtos[id-1]

            # Obter data e hora atual
            data = datetime.datetime.now()
            #data = data.strftime("%d do mês %m do ano %Y às %H horas e %M minutos")
            data = data.strftime("%d/%m/%Y às %H:%Mh")

            item = item+" - "+data

            vendas.append(item)

        # LISTAR (relatório)
        if resposta == "2":
            print("Lista de VENDAS do sistema:")
            for contador in range( len(vendas) ):
                print(f"{contador+1} - {vendas[contador]}")

    # LISTAR TODOS PRODUTOS
    if resposta == "3":
        # Percorrer uma lista
        print("Lista de produtos do sistema:")
        for contador in range( len(produtos) ):
            print(f"{contador+1} - {produtos[contador]}")

    # LISTAR UM PRODUTO ESPECÍFICO
    if resposta == "4":
        print("Digite o nome do produto:")
        nome = input()

        # Percorrer a lista PROCURANDO o produto
        for contador in range( len(produtos) ):
            # Verifica se é o produto digitado
            if produtos[contador] == nome:
                print("Produto encontrado!")
                print("Digite 1 para ALTERAR ou 2 para REMOVER:")
                resposta = input()

                # ALTERAR PRODUTO
                if resposta == "1":
                    print("Digite o NOVO NOME do produto:")
                    novo_nome = input()
                    # - Verificar se o novo nome é válido
                    produtos[contador] = novo_nome
                    print("Produto alterado com sucesso!")

                # REMOVER PRODUTO
                if resposta == "2":
                    produtos.remove( nome )
                    print("Produto removido com sucesso!")
            
                # Finalizar a operação para não ter problemas
                # na próxima repetição do FOR
                break



    # SAIR DO SISTEMA
    if resposta == "5":
        vendedor_esta_logado = False
        continue
        
        # print("Fim do sistema, até mais...")
        #break