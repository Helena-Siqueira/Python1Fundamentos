# LISTAS: atividade do estacionamento

lista_carros = [5]

while True:

    print("Lista de carros estacionados:")
    print(lista_carros)

    print("Opções do sistema:")
    print("1 - Estacionar")
    print("2 - Retirar")
    print("Digite uma opção:")
    resposta = int( input() )

    if resposta == 1:
        print("Digite a placa do veículo")
        placa = input()
        lista_carros.append(placa) 

    # elif resposta == 2:
    #    print("Certo, obrigada por utilizar nossos serviços")

    if resposta == 2:
        print("Digite a placa do veículo")
        placa = input()
        lista_carros.remove(placa) 

    