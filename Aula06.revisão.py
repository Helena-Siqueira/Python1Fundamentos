
#Cadastro de nomes

nome1 = ""
nome2 = ""
nome3 = ""

print("Bem-vindo ao cadastro de nomes. Vamos começar")

contador = 0
while contador < 3:

    print ("Digite o nome para cadastrar")
    resposta = input()
    nome1 = resposta

    if( nome1 == "" ):
        nome1 = resposta
    elif(nome2 == ""):
        nome2 = resposta
    elif(nome3 == ""):
        nome3 = resposta        

    contador += 1 

print("Obrigada por cadastrar os nomes")
print("Os nomes cadastrados foram:")
print(f"1 - {nome1}")
print(f"2 - {nome2}")
print(f"3 - {nome3}")