# Atividade do BANCO

saldo = 0


def main():

    global saldo

    print("Bem-vindo ao Conradito's Bank")
    print("Digite se deseja sacar ou depositar")
    resposta = input()

    # -- Verificar se opção é SACAR
    if resposta.lower() == "sacar":
    # Se for, pergunte o valor a sacar 
        print("Qual o valor que deseja sacar?")
        valor = int( input() )
    # Descontar o valor do saque no saldo 
        saldo -= valor

    # -- Verificar se opção é DEPOSITAR 
    if resposta.lower() == "depositar":
    # Se for, pergunte o valor do DEPOSITO
        print("Qual valor deseja depositar?")
        depositar = int( input() )
    # Aumentar o valor do deposito no SALDO
        saldo += valor

    # -- SEMPRE no final: 
    # Mostrar o valor do saldo
    print(f"Seu saldo final é de R$ {saldo}")
    # Reiniciar o sistema


main()


